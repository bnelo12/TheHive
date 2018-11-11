from socketIO_client import SocketIO, LoggingNamespace
import time

def handle_code(code):
    print('code:', code)
    time.sleep(2) 
    socketIO.emit('finished', '5')

with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    socketIO.on('code_send', handle_code)
    socketIO.wait(seconds=60)
