# P2 Execution Sequence Merger

This tool allows to merge the execution sequence of two (or more) ESO instruments (e.g., HARPS and NIRPS)
and to visualize the observability of the targets over the night.
It also keeps track of already observed targets.

## Installation

The p2esm package can be installed using pip with the following command:

``pip install p2esm``

## Settings

You first need to create a `p2esm.toml` config file.
The `p2esm` application looks for this file either in the current folder or in the `~/.config` folder.
A sample `p2esm.toml` is provided [here](https://gitlab.unige.ch/delisle/p2esm/-/blob/main/example/p2esm.toml).
Default parameters are set for observing with HARPS and NIRPS at La Silla.
The user and password should be the same as the ones used to login on the ESO P2 website.

## Usage

- Launch `p2esm` and login on P2 with your navigator.
- Add OBs in the execution sequences (in the navigator). You should see them appear in `p2esm`'s plot.
- Right click on the plot to set the observations starting time.
- Once the observations have started, `p2esm` keeps track of the currently running OB and the starting time should be updated automatically.
- Left click on an OB to switch instruments just after this OB.
- Black vertical lines highlight instrument changes.
- The red vertical line shows the current time.
- Already exectuted OBs are shown with pale colors. It may happen from time to time that an executed OB disappears (ticket open at ESO Helpdesk), it does not mean that the OB failed.
- Scheduled OBs that do not fulfill the airmass or moon separation constraints or cross the zenith are highlighted with dotted lines.
- `p2esm` is only a visualization tool. It does not affect the execution sequences in any way and it does not warn the TO of the instrument changes you schedule.
- You can close `p2esm`, reopoen it at any time. The execution sequences will be reloaded, but you will lose the scheduled instrument changes.

## Contribute

Everyone is welcome to open issues and/or contribute code via pull-requests.
A SWITCH edu-ID account is necessary to sign in to https://gitlab.unige.ch.
If you don't have an account, you can easily create one at https://eduid.ch.
Then you can sign in to https://gitlab.unige.ch by selecting "SWITCH edu-ID" as your organisation.
