# https://pypi.org/project/RPi.GPIO/
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

heater_on = 2
humidifier_switch = 25
blower_switch = 24
# Might need bounce on event, currently at 100ms
# Might need to switch pull_up_down to GPIO.PUD_UP
GPIO.setup(heater_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(humidifier_switch, GPIO.OUT)
GPIO.setup(blower_switch, GPIO.OUT)
GPIO.output(25, 0)
GPIO.output(24, 0)
print("Humidifier status:", GPIO.input(25))
print("Blower status:", GPIO.input(24))
global heater_status
heater_status = False
global heater_status_2
heater_status_2 = False
# this will run in another thread when the button is pushed 
#def heater_on_callback(channel):
#    print("Heater on")
#    global heater_status
#    heater_status = not heater_status
#    print(heater_status)
def heater_callback_timer(channel):
    print("Starting timer")
    count = 0
    sleep(1)
    if GPIO.input(2) == 0:
        global heater_status
        heater_status = True
    	while GPIO.input(2) == 0:
        	if count == 2:
	    	     global heater_status_2
            	     heater_status_2 = True
            	     break
        	else:
            	     sleep(1)
            	     count = count + 1
            	     print(count)
    else:
	while GPIO.input(2) == 1:
		global heater_status_2
		heater_status_2 = False
		if count == 2:
		     global heater_status
		     heater_status = False
                     break
		else:
		     sleep(1)
                     count = count + 1
                     print(count)
# Might need to change trigger condition to GPIO.FALLING or GPIO.BOTH
GPIO.add_event_detect(heater_on, GPIO.BOTH, callback=heater_callback_timer, bouncetime=1000)
#GPIO.add_event_detect(heater_on, GPIO.FALLING, callback=heater_off_callback, bouncetime=1000)
#while True:
#    if heater_status:
#        blink(humidifier_switch)

def blink(pin_id):
    GPIO.output(pin_id, True)
#    print("Humidifier turning on"
    sleep(2)
#    GPIO.output(pin_id, False)
#    print("Humdifier status:", GPIO.input(25))

while True:
      if heater_status == True:
             blink(humidifier_switch)
      else:
	     sleep(1)
      	     print("Humidifier is off")
	     GPIO.output(25, 0)
      if heater_status_2 == True:
            blink(blower_switch)
      else:
            sleep(1)
	    print("Blower is off")
            GPIO.output(24, 0)


#blink(humidifier_switch)

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
