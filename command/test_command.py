# ex: et sw=4 ts=4 sts=4

from command.command import Command

class TestCommand(Command):
    
    def __init__(self):
        super().__init__()
    
    def execute(self, handler):
        try:
            handler.write("Hello World!!")
        except Exception as e:
            self._logger.debug(e)
