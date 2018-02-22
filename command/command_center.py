# ex: et sw=4 ts=4 sts=4

import re
import threading

from base.singleton import Singleton
from command.list_command import TestCommand
from util.locker import Locker

# http path
HTTP_PATH_TEST          = r"/"

@Singleton
class CommandCenter:
    
    def init(self):
        self._lock = threading.Lock()
    
    def execute(self, handler):
        # get path
        path = handler.request.path
        # get correct controller
        if re.match(HTTP_PATH_TEST, path):
            locker = Locker(self._lock)
            command = TestCommand()
        else:
            command = None

        # start command
        if command:
            command.execute(handler)
