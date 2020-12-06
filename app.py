# Might need to use:
# https://pypi.org/project/RPi.GPIO/
import gpiozero
import config

from flask import Flask, request, make_response
from flask_cors import CORS

# Flask web server definition
webserver = Flask(__name__)
CORS(webserver)

@webserver.route('/pin/status', methods=['GET'])
def get_all_pin_status():

    status_code = 200
    message = "Pin status query successful!"
    data = [
        PinStatus(10, "Heater Status", True).to_json(),
        PinStatus(11, "Pump Status", False).to_json()
    ]

    dummy_response_data = {
        "status_code": status_code,
        "message": message,
        "data": data,
    }
    return make_response((dummy_response_data, status_code, None))

class PinStatus():

    def __init__(self, pin_number, device_name, status):
        self.pin_number = pin_number
        self.device_name = device_name
        self.status = status
    
    def to_json(self):
        return {
            "pin_number": self.pin_number,
            "device_name": self.device_name,
            "status": self.status
        }


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


if __name__ == '__main__':

    # Only create our actuator and sensor instances if mock_pi is set to False
    # mock_pi being set to False indicates that we should be connected to
    # the raspberry pi controller.
    if config.mock_pi == False:

        test_instance = Actuator("heater", 17)
        test_instance.activate()

        sensor_instance = Sensor("temperature", 21)

    # Start the webserver
    webserver.run(host="localhost", port=config.flask["port"], debug=config.flask["debug"])
    
