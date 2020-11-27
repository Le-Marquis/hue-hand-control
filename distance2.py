import RPi.GPIO as GPIO
from phue import Bridge
import time

bridge_ip_address = '192.168.88.92'

def testlight(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    lights = b.get_light_objects('id')
    return lights
    print('id')



GPIO.setwarnings(False)

# doing this first, since we're using a while True.

GPIO.cleanup()



GPIO.setmode(GPIO.BCM)

TRIG = 4

ECHO = 18



GREEN = 17

YELLOW = 27

RED = 22



GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)







def on():
    lights = testlight(bridge_ip_address)
    for light in lights:
        lights[12].on = True
        lights[24].on = True
        lights[25].on = True
        lights[24].brightness = 250
        lights[25].brightness = 250
        lights[12].brightness = 250




def mid():
    lights = testlight(bridge_ip_address)
    for light in lights:
        lights[12].on = True
        lights[24].on = True
        lights[25].on = True
        lights[12].brightness = 150
        lights[24].brightness = 150
        lights[25].brightness = 150

def low():
    lights = testlight(bridge_ip_address)
    for light in lights:
        lights[12].on = True
        lights[24].on = True
        lights[25].on = True
        lights[12].brightness = 50
        lights[24].brightness = 50
        lights[25].brightness = 50



def off():
    lights = testlight(bridge_ip_address)
    for light in lights:
        lights[12].on = False
        lights[24].on = False
        lights[25].on = False





def get_distance():





    GPIO.output(TRIG, True)

    time.sleep(0.00001)

    GPIO.output(TRIG, False)



    while GPIO.input(ECHO) == False:

        start = time.time()



    while GPIO.input(ECHO) == True:

        end = time.time()



    sig_time = end-start



    #CM:

    distance = sig_time / 0.000058



    #inches:

    #distance = sig_time / 0.000148

    #print('Distance: {} centimeters'.format(distance))



    return distance





while True:

    distance = get_distance()

    time.sleep(0.1)

#     print(distance)

    
    if 40 > distance > 30:

        on()

    elif 30 > distance > 20:

        mid()

    elif 20 > distance > 10:

        low()

    elif distance <= 10:

        off()