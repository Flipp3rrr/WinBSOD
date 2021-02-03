from distutils.core import setup
import py2exe, sys, os

sys.argv.append("py2exe")

setup(
    # Use "bundle_file": 1 to create a single EXE including everything
    # Use "compressed": True for a smaller file size
    options = {"py2exe": {"bundle_files": 1, "compressed": True}},
    windows = [{"script": "BSOD.py"}],
    zipfile = None,
    # Exclude tkinter because it's not needed
    excludes = ["Tkconstants","Tkinter","tcl"]
)