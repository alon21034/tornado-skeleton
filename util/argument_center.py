# ex: et sw=4 ts=4 sts=4

import sys

from base.singleton import Singleton

# key list
KEY_COMMAND = 'command'
KEY_PORT    = 'port'

@Singleton 
class ArgumentCenter:
    
    def __init__(self):
        # init param
        self._arguments = {};
        for i in range(2, len(sys.argv), 2):
            self._arguments[sys.argv[i - 1]] = sys.argv[i]
            
    def get(self, key):
        try:
            return self._arguments[key]
        except Exception as e:
            pass
        return None