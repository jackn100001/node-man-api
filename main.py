from flask import Flask, request
import os 
import json

app = Flask(__name__)

@app.route('/node/status')
def node_status():
    ip_address = request.args.get('ip_address')
    response = os.system("ping -c 1 " + str(ip_address))
    if response == 0:
        status = 'up'
    else:
        print(response)
        status = 'down'

    return status
