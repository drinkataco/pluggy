from flask import Flask, render_template, request, jsonify
from .pluggy import *

app = Flask(__name__, static_url_path='/pluggy/static')
pluggy = Pluggy()

"""
    Form index
"""
@app.route('/pluggy')
def index():
    plugs = pluggy.get_channels()
    actions = pluggy.get_actions()
    return render_template('index.html', plugs=plugs, actions=actions)

"""
    Change Switch Status
"""
@app.route('/pluggy/switch', methods=["POST"])
def change_switch():
    frequency = request.form.get('switch', type=int)
    on        = request.form.get('on', type=int)
    channel   = request.form.get('channel', type=str)

    if (pluggy.switch(channel, frequency, on)):
        return channel+','+str(frequency), 200
    else:
        return channel+','+str(frequency), 500
    
