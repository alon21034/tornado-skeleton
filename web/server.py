# ex: et sw=4 ts=4 sts=4

from concurrent import futures

from tornado import ioloop, web, gen

from command.command_center import CommandCenter, HTTP_PATH_TEST

from util.config import THREAD_COUNT
from util.log_util import Logger

import os

class AbstractHandler(web.RequestHandler):
    
    @gen.coroutine
    def get(self):
        # get thread pool
        pool = self.settings['pool']
        # send event to another thread
        yield pool.submit(CommandCenter.getInstance().execute, self)
        
class Server(object):
    
    def __init__(self):
        # set logger
        self._logger = Logger('server')
        # init command center
        CommandCenter.getInstance().init();
        self.root = os.path.dirname(__file__)
    
    def start(self, port):
        try:
            # init pool
            pool = futures.ThreadPoolExecutor(THREAD_COUNT)

            # init application
            application = web.Application(
                [
                    (HTTP_PATH_TEST, AbstractHandler),
                ],
                pool    = pool,
                debug   = True
            )
            
            # bind server
            application.listen(port)
            
            # start event loop
            self._logger.info('Start listening on port {0}'.format(port))
            ioloop.IOLoop.instance().start()

        except OSError as e:
            self._logger.debug(e)

    def stop(self):
        try:
            self._logger.info('Tornado server closing...')
            ioloop.IOLoop.instance().stop()
        except Exception as e:
            self._logger.debug(e)