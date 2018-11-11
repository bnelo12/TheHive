""" This is the Threading for hive """

import inspect
from textwrap import dedent
import sys
import subprocess
from tempfile import NamedTemporaryFile
import threading
from app import socketio
from app.socket import clients

thread_pool = []
client_number = 0

class HiveThread(object):
    """ This object exposes the threading API for TheHive """

    def __init__(self):
        self.finished = False
        self.result = None
        self.join_lock = threading.Condition()

    def join(self):
        """ This is the function to call to join threads """
        with self.join_lock:
            while not self.finished:
                self.join_lock.wait()

    def set_result(self, returned_result):
        """ This function is used by the content producer to propagate the result back """
        with self.join_lock:
            self.finished = True
            self.result += ', ' + returned_result
            self.join_lock.notifyAll()

    def get_result(self):
        """ This function can be used to get the value returned by the thread """
        if not self.finished:
            self.join()

        return self.result

    def run(self, thread, variable, i):
        """ This is the function that packages and sends off a thread. """
#         lines = dedent(inspect.getsource(self.main))
#         lines += """
# farg = {}
# kwargs = {}

# print(main(farg, **kwargs))

# """.format(farg, kwargs)

        code = 'x=' + str(variable) + '\n' + thread
        socketio.emit('code_send', code, room=clients[i])

    @staticmethod
    def main(farg, **kwargs):
        """ This is the function where the user writes the code """
        pass
