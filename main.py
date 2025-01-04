from gpiozero import DistanceSensor
import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D12, 16)


def green():
    for x in range(16):
        pixels[x] = (0,255,5)
def yellow():
    for x in range(16):
        pixels[x] = (255,125,0)
def red():
    for x in range(16):
        pixels[x] = (255,0,0)

def lightOff():
    for x in range(16):
        pixels[x] = (0,0,0)

def setup():
    sensor = DistanceSensor(echo=24, trigger=23,max_distance=3)
    
    distOLD= 5
    distNEW = 10

    counter = 0
    stillWorking = True

    for x in range(16):
        time.sleep(0.25)
        pixels[x] = (0,0,255)
    time.sleep(0.2)
    lightOff()
    for x in range(3):
        time.sleep(0.1)
        green()
        time.sleep(0.1)
        lightOff()
    time.sleep(1)

    while True:
        time.sleep(0.25)
        counter +=1
        distOLD=distNEW
        distNEW = sensor.distance * 100
        if abs(distOLD-distNEW) <5:
            distNEW=distOLD
        else:
            counter = 0
            stillWorking = True
        if stillWorking:
            if distNEW > 50:
                green()
            elif distNEW < 50 and distNEW > 25:
                yellow()
            elif distNEW < 25:
                red()
    
            if counter == 16:
                print('inactive')
                lightOff()
                stillWorking= False
    
setup()
   
