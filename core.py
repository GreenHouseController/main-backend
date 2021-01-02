# https://pypi.org/project/RPi.GPIO/
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

heater_on = 2
humidifier_switch = 25

# Might need bounce on event, currently at 100ms
# Might need to switch pull_up_down to GPIO.PUD_UP
GPIO.setup(heater_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(humidifier_switch, GPIO.OUT)

heater_status = False

# this will run in another thread when the button is pushed 
def heater_on_callback(channel):  
    print("Heater on")
    heater_status = not heater_status

# Might need to change trigger condition to GPIO.FALLING or GPIO.BOTH
GPIO.add_event_detect(heater_on, GPIO.RISING, callback=heater_on_callback)

#while True:
#    if heater_status == True:
#        blink(humidifier_switch)

def blink(pin_id):
    GPIO.output(pin_id, True)
    print("Humidifier turning on")
    sleep(5)
    GPIO.output(pin_id, False)

blink(humidifier_switch)

# class Actuator():

#     def __init__(self, kind, gpio_pin):

#         # TODO: Add if unit is wired or not
#         # Wired

#         # String "blower" or "heater"
#         self.kind = kind

#         # Boolean
#         self.active = False

#         # Mixed
#         self.gpio_pin = gpio_pin

#         self.led_instance = gpiozero.LED(self.gpio_pin)
#         self.deactivate()

#     def identifier_string(self):
#         return f"{self.kind} @ pin{self.gpio_pin}: "

#     def activate(self):
#         self.active = True
#         self.led_instance.on()
#         print(f"{self.identifier_string()}Activated")

#     def deactivate(self):
#         self.active = False
#         self.led_instance.off()
#         print(f"{self.identifier_string()}Deactivated")


# class Sensor():
#     def __init__(self, kind, gpio_pin):
#         self.kind = kind
#         self.gpio_pin = gpio_pin
#         def pushed () :
#             if self.kind == "ALARM":
#                 print ("sending email") 
#             else:
#                 print ("You pressed the button")
#                 print (self.kind)
#         self.button_instance = gpiozero.Button(self.gpio_pin)
#         self.button_instance.when_pressed = pushed
