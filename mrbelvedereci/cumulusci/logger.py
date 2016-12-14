""" mrbelvedereci logger """
# TODO:
#   - buffer to prevent saving too often
#   - disable transaction management?

import logging

import coloredlogs

from mrbelvedereci.cumulusci.exceptions import LoggerException


class LogStream(object):
    """ File-like interface to Django model. """

    def __init__(self, model):
        if not hasattr(model, 'log'):
            raise LoggerException('Model does not have "log" attribute.')
        self.model = model
        self.buffer = ''

    def flush(self):
        self.model.log += self.buffer
        self.model.save()
        self.buffer = ''

    def write(self, s):
        self.buffer += s


class LogHandler(logging.StreamHandler):
    """ Handle log messages. """

    def __init__(self, model):
        """ Initialize the handler. """
        Handler.__init__(self)
        self.stream = LogStream(model)


def init_logger(model):
    """ Initialize the logger. """

    formatter = coloredlogs.ColoredFormatter(fmt='%(asctime)s: %(message)s')

    handler = LogHandler(model)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger = logging.getLogger('cumulusci')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
