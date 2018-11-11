from threading import Thread

from eventlet import event, spawn
from flask import request
from flask_socketio import join_room, leave_room, emit, disconnect

from app import socketio
# from app import mongo

clients = []

@socketio.on('connect')
def on_connect():
    print('connected')
    return

@socketio.on('ready')
def on_ready():
    print('ready')
    clients.append(request.sid)
    return

@socketio.on('disconnect')
def disconnectSockets():
    return

import subprocess
from tempfile import NamedTemporaryFile
import sys
from app.hive_thread import HiveThread
import inspect

@socketio.on('webapp_code_send')
def getWebappCode(code):
    threads = []
    variables = []
    _locals = locals()
    exec(code, globals(), _locals)

    class Example(HiveThread):
        def __init__(self):
            HiveThread.__init__(self)

    print('sending code')

    example = Example()
    example.run(_locals['threads'], _locals['variables'])
    result = example.get_result()

    return

@socketio.on('finished')
def sendResult(result):
    socketio.emit('finished', result)
    return
