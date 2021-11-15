import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import waveFunctions as b


spi = spidev.SpiDev()

b.initSpiAdc()
##b.waitForOpen() second
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 1)
first
"""
data = []
count = 0
start = time.time()
timebreak = start
try:
    while (timebreak - start) < 10: ##30 second
        value = b.getAdc()
        count = count + 1
        data.append(value)
        timebreak = time.time()
finally:
    finish = timebreak
    samplesInMeasure = 6
    b.deinitSpiAdc()
    b.saveMeasures(data, count, samplesInMeasure, start, finish)
    b.showMeasures(data, count, samplesInMeasure, start, finish)
GPIO.cleanup()