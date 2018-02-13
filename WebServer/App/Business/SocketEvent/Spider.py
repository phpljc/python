import threading
from Business.JavBus import JavBus


class Spider():
    __options = None

    def __init__(self, options=None):
        self.__options = options

    def run(self):
        task = threading.Thread(target=self.threading, args=())
        task.start()

    def threading(self):
        JavBus(self.__options['pool'], self.sendMessage).run()

    def sendMessage(self, msg):
        self.__options['print']('spider', msg)
