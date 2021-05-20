from flask import Flask, request, jsonify                                                         
import threading
import core

data = 'foo'
app = Flask(__name__)

@app.route("/")
def main():
    return str(core.getHeaterStatus())

if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    threading.Thread(target=core.start).start()
    print ("duiwad")