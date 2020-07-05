from datetime import datetime
from threading import Timer
from goprocam import GoProCamera
from goprocam import constants
import starttimelapse
import time
import sys

# %% Establish time varibales
x=datetime.today()
print('current datetime',x)
y=x.replace(day=x.day, hour=18, minute=0, second=0, microsecond=0)
print('target datetime',y)
delta_t=y-x

secs=delta_t.seconds+1
print('time till target ',y-x)
print(secs)

# %% Interface with GoPro API
gpCam = GoProCamera.GoPro()
t = Timer(5, starttimelapse.starttimelapse, args = [gpCam])
t.start()
