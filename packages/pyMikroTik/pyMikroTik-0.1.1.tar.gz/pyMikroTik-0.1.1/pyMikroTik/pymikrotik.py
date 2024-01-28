import paramiko
import logging
from .ip import Ip
from .exceptions import ConnectError


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class MikroTikConnect:
    def __init__(self, host: str, login: str, password: str, port: int = 22,
                 auto_connection: bool = False,
                 ignore_errors: bool = False):
        self.host = host
        self.port = port
        self.__password = password
        self.__login = login
        self._auto_connection = auto_connection
        self._ignore_errors = ignore_errors
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.__client.connect(hostname=self.host, port=self.port, username=self.__login, password=self.__password)
            logging.info(f'Successful connection to {self.host}')
        except paramiko.ssh_exception.AuthenticationException:
            raise ConnectError('Ошибка аутентификации. Не верный логин или пароль')
        except paramiko.ssh_exception.NoValidConnectionsError:
            raise ConnectError(f'Не возможно подключится к хосту {self.host} по порту {self.port}')

    def disconnect(self):
        self.__client.close()

    @property
    def ip(self):
        return Ip(connection=self)

    @staticmethod
    def __check_connection(method):
        def wrapper(*args, **kwargs):
            if args[0]._auto_connection is False:
                return method(*args, **kwargs)
            try:
                funk = method(*args, **kwargs)
                return funk
            except AttributeError:
                args[0].connect()
                return method(*args, **kwargs)
        return wrapper

    @__check_connection
    def send_command(self, command) -> str:
        """Принимает комманду. Возвращает ответ"""
        _, stdout, __ = self.__client.exec_command(command)
        output = stdout.read().decode('utf-8')
        return output

