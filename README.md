# WinBSOD
A "harmless" EXE file to get a BSOD.
## Dependencies
* py2exe
* Firefox (on the target machine)
## Downloading
Simply download the zipped EXE file from the [releases](https://github.com/Flipp3rrr/WinBSOD/releases) and place it wherever you want.
## Building
Run `python setup.py` to create the EXE
## Help needed
Currently we use `imp.is_frozen` in the detection wether or not the you're running an EXE file. The `imp` module is deprecated and I'm looking into an alternative, if anyone could help with this it would be greatly appreciated.
