import inspect
import re
from app import socketio
import types

@types.coroutine
def map(func, callback):
    funcString = inspect.getsource(func)
    matchObj = re.match(r'map\((.*)\)', funcString, re.M|re.I|re.MULTILINE)
    socketio.emit(matchObj.group(1))
    socketio.on('finished', lambda result: callback(result))
    pass

def reduce(func):

    pass
