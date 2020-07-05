from datetime import datetime
from threading import Timer
from goprocam import GoProCamera
from goprocam import constants
import gopro-functions
import time
import sys

# %% Establish time varibales
x=datetime.today()
print('Current datetime:',x.strftime('%H:%M:%S'))
y=x.replace(day=x.day, hour=18, minute=0, second=0, microsecond=0)
print('Target datetime:',y.strftime('%H:%M:%S'))
delta_t=y-x

print('Time till target (hh:mm:ss):',str(delta_t).split('.')[0])

# %% Interface with GoPro API
gpCam = GoProCamera.GoPro()
t = Timer(delta_t.seconds, starttimelapse.starttimelapse, args = [gpCam])
t.start()
