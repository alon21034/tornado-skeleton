# ex: et sw=4 ts=4 sts=4

import sys, time, signal

from web.server import Server
from util.argument_center import ArgumentCenter, KEY_COMMAND, KEY_PORT
from util.log_util import Logger, setup_logger
from util.config import HTTP_PORT

server = Server()

def sig_exit(signum, frame):
    server.stop()

def main():
    if ArgumentCenter.getInstance().get(KEY_COMMAND):
        pass
    else:
        # port
        port = ArgumentCenter.getInstance().get(KEY_PORT) if ArgumentCenter.getInstance().get(KEY_PORT) else HTTP_PORT
        
        # setup logger
        setup_logger();
    
        # signal handler
        signal.signal(signal.SIGINT, sig_exit)

        # start server thread
        server.start(HTTP_PORT)

if __name__ == "__main__":
    main()
