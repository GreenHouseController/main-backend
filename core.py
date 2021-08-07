# https://pypi.org/project/RPi.GPIO/
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
main_power_on = 2
heater_on = 3
blower_on = 4
dehumidifier_on = 17
sump_pump_on = 27
hi_level_alarm_on = 22
test_charge = 5

humidifier_switch = 25
blower_switch = 24
heater_switch = 23
# Might need bounce on event, currently at 100ms
# Might need to switch pull_up_down to GPIO.PUD_UP
GPIO.setup(heater_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(main_power_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blower_on, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dehumidifier_on, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sump_pump_on, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(hi_level_alarm_on, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(test_charge, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(humidifier_switch, GPIO.OUT)
GPIO.setup(blower_switch, GPIO.OUT)
GPIO.setup(heater_switch, GPIO.OUT)
#GPIO.setup(sump_pump_switch, GPIO.OUT)
GPIO.output(25, 0)
GPIO.output(24, 0)
GPIO.output(23, 0)
print("Humidifier status:", GPIO.input(25))
print("Blower status:", GPIO.input(24))
global heater_status
heater_status = False
global main_power_status
main_power_status = False
global blower_status
blower_status = False
global dehumidifier_status
dehumidifier_status = False
global sump_pump_status
sump_pump_status = False
global hi_level_alarm_status
hi_level_alarm_status = False
# this will run in another thread when the button is pushed 
#def heater_on_callback(channel):
#    print("Heater on")
#    global heater_status
#    heater_status = not heater_status
#    print(heater_status)
def main_power_callback(channel):
    sleep(1)
    if GPIO.input(main_power_on) == 0:
        global main_power_status
        main_power_status = True
        print (main_power_status)
    else:
        global main_power_status
        main_power_status = False

def heater_callback(channel):
    sleep(1)
    if GPIO.input(heater_on) == 0:
        global heater_status
        heater_status = True
    else:
        global heater_status
        heater_status = False
        
def blower_callback(channel):
    print("blower callback")
    sleep(1)
    print (GPIO.input(blower_on))
    if GPIO.input(blower_on) == 0:
        print("blower callback is true")
        global blower_status
        blower_status = True
    else:
        print("blower callback is false")
        global blower_status
        blower_status = False
             
def dehumidifier_callback(channel):
    print("blower callback")
    sleep(1)
    print (GPIO.input(dehumidifier_on))
    if GPIO.input(dehumidifier_on) == 0:
        print("dehumidifier callback is true")
        global dehumidifier_status
        dehumidifier_status = True
    else:
        print("dehumidifier callback is false")
        global dehumidifier_status
        dehumidifier_status = False
        
def sump_pump_callback(channel):
    sleep(1)
    if GPIO.input(sump_pump_on) == 0:
        global sump_pump_status
        sump_pump_status = True
    else:
        global sump_pump_status
        sump_pump_status = False
        
def hi_level_alarm_callback(channel):
    sleep(1)
    if GPIO.input(hi_level_alarm_on) == 0:
        global hi_level_alarm_status
        hi_level_alarm_status = True
    else:
        global hi_level_alarm_status
        hi_level_alarm_status = False
        
def test_callback(channel):
    print ("RECIEVED INPUT")
# Might need to change trigger condition to GPIO.FALLING or GPIO.BOTH
GPIO.add_event_detect(main_power_on, GPIO.BOTH, callback=main_power_callback, bouncetime=1000)
GPIO.add_event_detect(heater_on, GPIO.BOTH, callback=heater_callback, bouncetime=1000)
GPIO.add_event_detect(blower_on, GPIO.BOTH, callback=blower_callback, bouncetime=1000)
GPIO.add_event_detect(dehumidifier_on, GPIO.BOTH, callback=dehumidifier_callback, bouncetime=1000)
GPIO.add_event_detect(sump_pump_on, GPIO.BOTH, callback=sump_pump_callback, bouncetime=1000)
GPIO.add_event_detect(hi_level_alarm_on, GPIO.BOTH, callback=hi_level_alarm_callback, bouncetime=1000)
GPIO.add_event_detect(test_charge, GPIO.BOTH, callback=test_callback, bouncetime=1000)
#GPIO.add_event_detect(heater_on, GPIO.FALLING, callback=heater_off_callback, bouncetime=1000)

        
def getHeaterStatus():
    return heater_status

def getMainPowerStatus():
    return main_power_status

def getBlowerStatus():
    return blower_status

def getDehumidifierStatus():
    return dehumidifier_status

def getSumpPumpStatus():
    return sump_pump_status

def getHiLevelStatus():
    return hi_level_alarm_status

def blinkPinNumber(pin,status):
    if status==True:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)
