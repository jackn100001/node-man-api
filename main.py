from flask import Flask, request
import os 
import json

app = Flask(__name__)

@app.route('/node/status')
def node_status():
    hostname = request.args.get('hostname')
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        status = json.loads('{ "status": "up" }')
    else:
        print(response)
        status = json.loads('{ "status": "down" }')

    return status
