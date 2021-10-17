from djitellopy import Tello
import time
import librosa
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd


def fly_polly(sides, drone):
    for s in range (sides):
        rotateangel = (round(360/sides))
        tello.rotate_clockwise(rotateangel)
        tello.move_forward(21)

def DrawSoundTicks(file):
    ipd.Audio(file)
    ipd.display()
    y, sr = librosa.load(file, sr=None)

    plt.figure(figsize=(16, 4))
    librosa.power_to_db
    librosa.display.waveplot(y, sr=sr)
    plt.show()


#=========================

"""
fname = 'c:/boom.flac'
DrawSoundTicks(fname)
"""
tello = Tello()
#tello.TIME_BTW_COMMANDS = 4

tello.connect()
tello.get_battery()
time.sleep(4)
tello.takeoff()
time.sleep(6)
#fly_polly(3, tello)

tello.move_left(22)

#tello.rotate_counter_clockwise(90)

#tello.move_forward(100)
time.sleep(4)
tello.land()