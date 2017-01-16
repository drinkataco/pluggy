from flask import Flask, render_template, request, jsonify
from .pluggy import *

app = Flask(__name__, static_url_path='/pluggy/static')
pluggy = Pluggy()

@app.route('/pluggy')
def index():
    """
        Form index
    """
    plugs = pluggy.get_channels()
    actions = pluggy.get_actions()
    return render_template('index.html', plugs=plugs, actions=actions)

@app.route('/pluggy/switch', methods=["POST"])
def call_switch():
    """
        Change Switch Status
    """
    frequency = request.form.get('switch', type=int)
    on        = request.form.get('on', type=int)
    channel   = request.form.get('channel', type=str)

    if (pluggy.switch(channel, frequency, on)):
        return channel+','+str(frequency), 200
    else:
        return channel+','+str(frequency), 500
    
@app.route('/pluggy/action', methods=["POST"])
def call_action():
    """
        Call Switch Action
    """
    action = request.form.get('action', type=str)

    if (pluggy.action(action)):
        return '', 200
    else:
        return '', 500