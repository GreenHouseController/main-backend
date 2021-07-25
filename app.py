import config
import core
from core import *
import threading
from flask import Flask, request, make_response, Response, jsonify
from flask_cors import CORS
#from flask.ext.cors import CORS, cross_origin
# from flask_socketio import SocketIO

status_list = [
    {'Heater': 0,
     'Blower' : 0,},
]


# Flask web server definition
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    status_list[0]['Heater'] = core.getHeaterStatus()
    status_list[0]['Blower']= core.getBlowerStatus()
    status_list[0]['Simultaneous']=core.getSimultaneousStatus()
    return jsonify(status_list)
#jsonify(core.getHeaterStatus())

@app.route('/Inputs', methods=['GET', 'POST'])
def get_all_inputs():
    data = request.data
    print (data)
    #return data
    data1 = data.split(":")[1]
    data2 = data.split(":")[3]
    print (data1)
    print (data2)
    if data1 == "false":
        blinkPinNumber(24,False)
    elif data1 == "true":
        blinkPinNumber(24,True)
    if data2 == "false":
        blinkPinNumber(25,False)
    elif data2 == "true":
        blinkPinNumber(25,True)
    return(data)
    
    
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

# Socket server definition
# socket_server = SocketIO(webserver)

# @socket_server.on('connect')
# def client_connected():
#     print('Client connected')
#     emit('connected', {'data': 'Connected'})

# @socket_server.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# # Used for sending messages to the frontend
# def send_message(payload):
#     emit('message', payload, broadcast=True)
pin = 24
status = True

if __name__ == '__main__':
    kwargs = {'host': '0.0.0.0', 'port': 5000, 'threaded' : True, 'use_reloader':False, 'debug': True}
    threading.Thread(target=app.run, kwargs=kwargs).start()
    threading.Thread(target=core.start).start()
    print ("duiwad")
    # Only create our actuator and sensor instances if mock_pi is set to False
    # mock_pi being set to False indicates that we should be connected to
    # the raspberry pi controller.
    if config.mock_pi == False:

        test_instance = core.Actuator("heater", 17)
        test_instance.activate()
        console.log("hi")

        sensor_instance = core.Sensor("temperature", 21)
        if sensor_instance.button_instance.value == 1:
            status_list.append("Heater is on")
        else:
            status_list.append("Heater is off")
        alarm_instance = Sensor("ALARM", 26)
        if alarm_instance.button_instance.value == 1:
            status_list.append("Alarm is on")
        else:
             status_list.append("Alarm is off")
    # Start the webserver
    # socket_server.run(webserver, host="localhost", port=config.flask["port"], debug=config.flask["debug"])
    
