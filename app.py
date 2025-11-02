from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return jsonify({
        "message": "Hello from Python app running on GKE!",
        "hostname": hostname
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
