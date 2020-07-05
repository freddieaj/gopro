from datetime import datetime
from goprocam import GoProCamera
from goprocam import constants
import time
import sys

def starttimelapse(gpCam):
    print('\n')
    gpCam.mode(constants.Mode.MultiShotMode, constants.Mode.SubMode.MultiShot.TimeLapse) #change mode to multishot and sub-mode to timelapse
    gpCam.gpControlSet(constants.Multishot.TIMELAPSE_INTERVAL, constants.Multishot.TimeLapseInterval.I30) #change time lapse interval to 30 seconds

    gpCam.overview() #Print a simple overview of camera

    print('\nTimelapse initiated at', datetime.today().strftime('%Y-%m-%d'))
    gpCam.shutter(constants.start) #Starts capture
