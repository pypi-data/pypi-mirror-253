# -*- coding: utf-8 -*-

# Copyright 2024 Jean-Baptiste Delisle
#
# This file is part of p2esm.
#
# p2esm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# p2esm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with p2esm.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import tkinter as tk
from datetime import datetime, timedelta, timezone

import numpy as np
import p2api
from matplotlib import rcParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.dates import DateFormatter, num2date
from matplotlib.figure import Figure

if sys.version_info >= (3, 11):
  import tomllib
else:
  import tomli as tomllib


def dms2deg(dms):
  neg = dms.startswith('-')
  sp = dms[neg:].split(':')
  return (1 - 2 * neg) * (float(sp[0]) + float(sp[1]) / 60 + float(sp[2]) / 3600)


class P2ESM(tk.Tk):
  def __init__(self, config):
    super().__init__()
    self.iconphoto(
      True,
      tk.PhotoImage(file=f'{os.path.dirname(os.path.realpath(__file__))}/p2esm.png'),
    )
    self.config = config
    self.inst = self.config['telescope']['instruments']
    self.ninst = len(self.inst)
    self.wm_title('P2 Execution Sequence Merger')
    self.init_widgets()
    self.init_p2api()
    self.refresh_p2()
    self.redraw()

  def init_widgets(self):
    rcParams.update({'font.size': self.config['plot']['fontsize']})
    self.fig = Figure(
      figsize=self.config['plot']['figsize'], dpi=self.config['plot']['dpi']
    )
    self.ax = self.fig.add_subplot()
    self.canvas = FigureCanvasTkAgg(self.fig, master=self)
    self.canvas.draw()
    self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    self.canvas.mpl_connect('button_press_event', self.on_click)

  def on_click(self, event):
    if not self.initialized or event.xdata is None:
      return
    ut = num2date(event.xdata)
    if event.button == 1:
      starts = np.array([ob['start'] for ob in self.sequence])
      k = np.searchsorted(starts, ut) - 1
      if k == -1:
        self.current_inst = (self.current_inst + 1) % self.ninst
        self.next_inst = self.current_inst
      elif k < len(self.sequence) - 1:
        obId = self.sequence[k]['obId']
        inst = self.sequence[k]['inst']
        if obId in self.switch:
          inst = self.switch[obId]
        self.switch[obId] = (inst + 1) % self.ninst
        if self.switch[obId] == self.sequence[k]['inst']:
          self.switch.pop(obId)
    else:
      self.start = ut
      self.custom_start = True
      self.custom_start_expiry = self.now + timedelta(seconds=10)

  def init_p2api(self):
    self.p2api = p2api.ApiConnection(
      self.config['p2api']['env'],
      self.config['p2api']['user'],
      self.config['p2api']['password'],
    )
    if self.config['telescope']['site'].lower().startswith('paranal'):
      # Paranal
      self.obs_site = {
        'lat': -24.627439409999997,
        'lon': -70.40498688000002,
      }
    else:
      # La Silla
      self.obs_site = {
        'lat': -29.25666666666666,
        'lon': -70.73,
      }
    self.now = datetime.now(tz=timezone.utc)
    tshift = timedelta(hours=self.obs_site['lon'] / 360 * 24)
    self.night = (
      (
        self.now
        + tshift
        - timedelta(hours=self.config['telescope']['latest_localtime_sunrise_h'])
      )
      .date()
      .isoformat()
    )
    self.initialized = False
    self.current_ob = None
    self.current_inst = 0
    self.next_inst = 0
    self.switch = {}
    self.custom_start = False
    self.start = None
    self.sequence = []
    self.known_ob = {}
    self.known_visibility = {}

  def get_ob(self, obId):
    if obId not in self.known_ob:
      try:
        self.known_ob[obId] = self.p2api.getOB(obId)[0]
      except p2api.P2Error:
        self.known_ob[obId] = {'obId': obId, 'itemType': 'No access'}
    return self.known_ob[obId]

  def get_visibility(self, ob):
    if ob['obId'] not in self.known_visibility:
      vis = self.p2api.post(
        '/visibility', {'night': self.night, 'targets': [{'obId': ob['obId']}]}
      )[0]
      if not self.initialized:
        self.sunset = datetime.fromisoformat(vis['night']['sunset'])
        self.nautical_night_start = datetime.fromisoformat(vis['night']['nauticalDusk'])
        self.astro_night_start = datetime.fromisoformat(vis['night']['start'])
        self.astro_night_end = datetime.fromisoformat(vis['night']['end'])
        self.nautical_night_end = datetime.fromisoformat(vis['night']['nauticalDawn'])
        self.sunrise = datetime.fromisoformat(vis['night']['sunrise'])
        self.t = np.array([datetime.fromisoformat(dk['time']) for dk in vis['data']])
        self.dt = self.t[1] - self.t[0]
        self.moon_alt = np.array([dk['moon']['elevation'] for dk in vis['data']])
        self.start = self.sunset
        self.initialized = True
      obIdstr = str(ob['obId'])
      hem = 'North' if dms2deg(ob['target']['dec']) > self.obs_site['lat'] else 'South'
      alt = np.array([dk[obIdstr]['elevation'] for dk in vis['data']])
      airmass = np.array([dk[obIdstr]['airmass'] for dk in vis['data']])
      airmass[airmass < 0] = np.inf
      moon_sep = np.array([dk[obIdstr]['moonDistance'] for dk in vis['data']])
      crosses_zenith = np.array([dk[obIdstr]['crossesZenith'] for dk in vis['data']])
      self.known_visibility[ob['obId']] = hem, alt, airmass, moon_sep, crosses_zenith
    return self.known_visibility[ob['obId']]

  def add_ob(self, ob, inst):
    ob_start = self.end
    self.end = ob_start + timedelta(seconds=ob['executionTime'])
    hem, alt, airmass, moon_sep, crosses_zenith = self.get_visibility(ob)
    trange = (self.t + self.dt / 2 >= ob_start) & (self.t - self.dt / 2 < self.end)

    max_airmass = np.max(airmass[trange]) if np.any(trange) else np.inf
    min_moon_sep = np.min(moon_sep[trange]) if np.any(trange) else 0
    any_crosses_zenith = np.any(crosses_zenith[trange]) if np.any(trange) else False

    err = ''
    if max_airmass > ob['constraints']['airmass']:
      err += f"⚠ airmass {max_airmass:.2f} > { ob['constraints']['airmass']} "
    if min_moon_sep < ob['constraints']['moonDistance']:
      err += f"⚠ moon {min_moon_sep:.2f} < { ob['constraints']['moonDistance']} "
    if any_crosses_zenith:
      err += '⚠ crosses zenith '
    if err:
      err += '- '
    lbl = f"{err}{hem} - {self.inst[inst]} - {ob['target']['name']}"
    self.sequence.append(
      {
        'label': lbl,
        'ok': err == '',
        'start': ob_start,
        'end': self.end,
        'trange': trange,
        'alt': alt,
        'switch': None,
        'obId': ob['obId'],
        'inst': inst,
      }
    )

  def refresh_p2(self):
    self.new_ess = [
      self.p2api.getExecutionSequence(self.inst[k])[0] for k in range(self.ninst)
    ]
    if not self.initialized:
      for inst in range(self.ninst):
        if self.new_ess[inst]:
          self.get_visibility(self.new_ess[inst][0])
          break
    nes = sum(
      [
        [
          (ex, self.get_ob(ex['obId']))
          for ex in self.p2api.getNightExecutions(self.inst[k], self.night)[0]
          if ex['obStatus'] == 'X'
        ]
        for k in range(self.ninst)
      ],
      [],
    )
    k = 0
    while not self.initialized and k < len(nes):
      if nes[k][1]['itemType'] == 'OB':
        self.get_visibility(nes[k][1])
      k += 1

    self.new_nes = sorted(
      [
        (
          ob['target']['name'],
          (self.t + self.dt / 2 >= datetime.fromisoformat(ex['from']))
          & (self.t - self.dt / 2 < datetime.fromisoformat(ex['to'])),
        )
        + self.get_visibility(ob)
        for ex, ob in nes
        if ob['itemType'] == 'OB'
      ],
      key=lambda x: x[1][0],
    )

    self.after(self.config['p2api']['update_interval_ms'], self.refresh_p2)

  def refresh_sequence(self):
    self.now = datetime.now(tz=timezone.utc)
    if not self.initialized:
      return
    if self.new_ess is not None:
      self.ess = self.new_ess
      self.nes = self.new_nes
      self.new_ess = None
      self.new_nes = None

    lens = [len(self.ess[k]) for k in range(self.ninst)]
    is_observing = False
    for k in range(self.ninst):
      if lens[k] > 0:
        if self.ess[k][0]['obStatus'] == 'S':
          if self.current_ob != self.ess[k][0]['obId'] or self.custom_start:
            self.current_ob = self.ess[k][0]['obId']
            execs, _ = self.p2api.getOBExecutions(
              self.current_ob, self.now.strftime('%Y-%m-%d')
            )
            if execs:
              self.start = datetime.fromisoformat(execs[-1]['from'])
            else:
              self.start = self.now
          is_observing = True
          self.custom_start = False
          self.current_inst = k
          self.next_inst = self.switch.get(self.current_ob, k)

    if (
      self.custom_start
      and self.now > self.start
      and self.now > self.custom_start_expiry
    ):
      self.custom_start = False

    if not is_observing and not self.custom_start:
      self.start = max(self.now, self.sunset)
      self.current_inst = self.next_inst
    inds = [0 for k in range(self.ninst)]
    inst = self.current_inst
    self.sequence = []
    self.end = self.start
    nobs = np.sum(lens)
    while len(self.sequence) < nobs:
      if lens[inst] > inds[inst]:
        if self.sequence:
          self.sequence[-1]['switch'] = (
            inst if self.sequence[-1]['inst'] != inst else None
          )
        ob = self.ess[inst][inds[inst]]
        inds[inst] += 1
        self.add_ob(ob, inst)
        if ob['obId'] in self.switch:
          inst = self.switch[ob['obId']]
      else:
        inst = (inst + 1) % self.ninst
    if nobs > 0:
      self.current_inst = self.sequence[0]['inst']

  def redraw(self):
    self.refresh_sequence()
    if self.initialized:
      self.ax.cla()
      self.ax.set_xlim(self.sunset, self.sunrise)
      self.ax.set_ylim(0, 90)
      self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
      self.ax.set_xlabel('UT')
      self.ax.set_ylabel('Elevation (⁰)')
      self.ax.fill_between(
        [self.sunset, self.sunrise],
        2 * [0],
        2 * [90],
        color='lightgray',
        label='civil and nautical twilights',
      )
      self.ax.fill_between(
        [self.nautical_night_start, self.nautical_night_end],
        2 * [0],
        2 * [90],
        color='darkgray',
        label='astronomical twilight',
      )
      self.ax.fill_between(
        [self.astro_night_start, self.astro_night_end], 2 * [0], 2 * [90], color='white'
      )
      self.ax.plot(
        self.t,
        self.moon_alt,
        '-.',
        c='blue',
        lw=2,
        label='Moon',
        rasterized=True,
      )
      self.ax.axvline(x=self.now, c='r', lw=1.5)
      for name, trange, _, alt, _, _, _ in self.nes:
        self.ax.plot(
          self.t,
          alt,
          '--',
          c='gray',
          lw=0.5,
          alpha=0.35,
          rasterized=True,
        )
        self.ax.plot(
          self.t[trange],
          alt[trange],
          '-',
          lw=1.5,
          alpha=0.35,
          label=f'✓ {name}',
          rasterized=True,
        )
      if self.start < self.sunrise:
        self.ax.axvline(x=self.start, c='k', ls='--')
        self.ax.text(
          self.start + timedelta(minutes=5),
          89,
          self.inst[self.current_inst],
          rotation='vertical',
          horizontalalignment='left',
          verticalalignment='top',
        )
      for ob in self.sequence:
        self.ax.plot(
          self.t,
          ob['alt'],
          '--',
          c='gray',
          lw=0.5,
          rasterized=True,
        )
        self.ax.plot(
          self.t[ob['trange']],
          ob['alt'][ob['trange']],
          '-' if ob['ok'] else ':',
          lw=1.5 if ob['ok'] else 3,
          label=ob['label'],
          rasterized=True,
        )
        if ob['switch'] is not None and np.any(ob['trange']):
          self.ax.axvline(x=self.t[ob['trange']][-1], c='k')
          self.ax.text(
            self.t[ob['trange']][-1] + timedelta(minutes=5),
            89,
            self.inst[ob['switch']],
            rotation='vertical',
            horizontalalignment='left',
            verticalalignment='top',
          )
      self.ax.legend(bbox_to_anchor=(1, 0.5), loc='center left')
      self.ax.set_title(
        f'Current time (UT): {self.now.strftime("%Y-%m-%d %H:%M:%S")}'
        + self.config['plot']['title_space'] * ' '
        + f'Start (UT): {self.start.strftime("%Y-%m-%d %H:%M:%S")}'
        + self.config['plot']['title_space'] * ' '
        + f'End (UT): {self.end.strftime("%Y-%m-%d %H:%M:%S")}'
      )
    else:
      self.ax.set_title(
        'Please add an OB to the execution sequence to initialize p2esm'
      )
      self.ax.axis('off')
    self.fig.tight_layout(pad=0.5)
    self.canvas.draw()
    self.after(self.config['plot']['update_interval_ms'], self.redraw)


def main():
  config = None

  paths = ['p2esm.toml', os.path.expanduser('~/.config/p2esm.toml')]
  for path in paths:
    if os.path.exists(path):
      config = tomllib.load(open(path, 'rb'))
      break

  if config is None:
    raise Exception(f'Could not find any config file in {paths}')

  P2ESM(config).mainloop()
