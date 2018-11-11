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


@socketio.on('webapp_code_send')
def getWebappCode(code):
    from app.hive_thread import HiveThread

    class Example(HiveThread):
        def __init__(self):
            HiveThread.__init__(self)

        def main(self, farg, **kwargs):
            return(farg + kwargs["arg2"])

    print('sending code')

    example = Example()
    example.run(2, arg2=3)
    result = example.get_result()
    socketio.emit('finished', result)
    return

@socketio.on('finished')
def sendResult(result):
    socketio.emit('finished', result)
    return
