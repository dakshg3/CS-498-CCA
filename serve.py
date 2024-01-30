from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Started stress_cpu.py"

    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return f"{private_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
