from threading import Timer
from goprocam import GoProCamera
from goprocam import constants
import goprofunctions
import datetime
import time
import sys

# %% Establish time varibales
print('')
while True:
    try:
        string = input('specify a delay time in format HH:MM:SS - ').split(':')
        delay = datetime.timedelta(seconds = int(string[0])*3600 + int(string[1])*60 + int(string[2])) #parse input to a timedelta object

    except ValueError:
        print("Sorry, I didn't understand that input.")
    else:
        break

# %% Summarise timelapse config to user
print('')
print(datetime.datetime.today().strftime('%H:%M:%S'), ' = current time')
delay_str = str(delay)
if len(delay_str) < 8: delay_str = '0'+delay_str #pad timedelta value with a 0 if needed to satisfy my OCD
print(delay_str, ' = time till target (hh:mm:ss) \n' )

# %% Interface with GoPro API
gpCam = GoProCamera.GoPro() # Connect to GoPro on current network
t = Timer(delay.seconds, goprofunctions.starttimelapse, args = [gpCam]) # Define a timer that calls the time lapse function
t.start() # start the timer
