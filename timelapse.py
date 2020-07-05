from threading import Timer
from goprocam import GoProCamera
from goprocam import constants
import goprofunctions
import datetime
import time
import sys

# %% Establish time varibales
#x=datetime.today()
#print('Current datetime:',x.strftime('%H:%M:%S'))
#y=x.replace(day=x.day, hour=18, minute=0, second=0, microsecond=0)
#print('Target datetime:',y.strftime('%H:%M:%S'))
#delta_t=y-x

while True:
    try:
        delta_t = 3600*float(input("Please enter a delay time in decimal hours (e.g 1.5): "))
    except ValueError:
        #Some error in input
        print("Sorry, I didn't understand that input.")
        continue
    else:
        #delay successfully parsed
        break

print('Time till target (hh:mm:ss):', datetime.timedelta(seconds = delta_t))

# %% Interface with GoPro API
gpCam = GoProCamera.GoPro()
t = Timer(delta_t, goprofunctions.starttimelapse, args = [gpCam])
t.start()
