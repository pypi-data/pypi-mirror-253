import logging
from functools import wraps


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class PyMikroTikExceptions(Exception):
    pass


class ConnectError(PyMikroTikExceptions):
    pass


class IpAddressFormatError(PyMikroTikExceptions):
    pass


class RouterError(PyMikroTikExceptions):
    pass


class InvalidSearchAttribute(PyMikroTikExceptions):
    pass


def exception_control(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        if args[0].connection._ignore_errors is False:
            return method(*args, **kwargs)
        try:
            return method(*args, **kwargs)
        except PyMikroTikExceptions as err:
            logging.error(err)
            return err
    return wrapper
