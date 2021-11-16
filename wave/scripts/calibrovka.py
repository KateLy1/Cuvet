import spidev
import RPi.GPIO as GPIO

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC have been initialized")


def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")


def getAdc():
    adcResponse = spi.xfer2([0, 0])
    adc = ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1
    return adc


def getMeanAdc(samples):
    sum = 0
    for i in range(samples):
        sum += getAdc()
    
    return int(sum / samples)


initSpiAdc()

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 1)
data = []
samples = 1000
value = getMeanAdc(samples)
data.append(value)
str_mass=[str(i) for i in data]
with open("100calibrovkamm.txt","w") as outfile:
    outfile.write("\n".join(str_mass))

GPIO.cleanup()

deinitSpiAdc()
