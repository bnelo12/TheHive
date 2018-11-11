from threading import Thread

from eventlet import event, spawn
from flask import request
from flask_socketio import join_room, leave_room, emit, disconnect

from app import socketio
# from app import mongo

@socketio.on('connect')
def on_connect():
    print('connected')
    return

@socketio.on('disconnect')
def disconnect():
    return

@socketio.on('webapp_code_send')
def getWebappCode(code):
    print('sending code')
    socketio.emit('code_send', code)
    return

@socketio.on('finished')
def getWebappCode(result):
    socketio.emit('finished', result)
    return
