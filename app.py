# Might need to use:
# https://pypi.org/project/RPi.GPIO/
import gpiozero

import config

class Actuator():

    def __init__(self, kind, gpio_pin):

        # TODO: Add if unit is wired or not
        # Wired

        # String "blower" or "heater"
        self.kind = kind

        # Boolean
        self.active = False

        # Mixed
        self.gpio_pin = gpio_pin

        self.led_instance = gpiozero.LED(self.gpio_pin)
        self.deactivate()

    def identifier_string(self):
        return f"{self.kind} @ pin{self.gpio_pin}: "

    def activate(self):
        self.active = True
        self.led_instance.on()
        print(f"{self.identifier_string()}Activated")

    def deactivate(self):
        self.active = False
        self.led_instance.off()
        print(f"{self.identifier_string()}Deactivated")


class Sensor():
    def __init__(self, kind, gpio_pin):
        self.kind = kind
        self.gpio_pin = gpio_pin
        self.button_instance = gpiozero.Button(self.gpio_pin)
        self.button_instance.wait_for_press()
        print("button pressed")

test_instance = Actuator("heater", 17)
test_instance.activate()

sensor_instance = Sensor("temperature", 21)