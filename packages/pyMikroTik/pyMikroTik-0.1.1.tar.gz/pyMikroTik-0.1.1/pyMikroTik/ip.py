from .entities import MTObject, IPAddress
import logging
from .exceptions import exception_control, RouterError, InvalidSearchAttribute
import re


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class Address(MTObject):
    """/ip address (object)"""
    def __init__(self, connection):
        self.connection = connection
        self.address: IPAddress or None = None
        self.network: IPAddress or None = None
        self.interface: str or None = None
        self.comment: str or None = None
        self.numbers: str or None = None

        self.disabled: bool = False
        self.flags: str or None = None
        self.__number: int or None = None

    @exception_control
    def add(self, address: str, interface: str, network: str = None, comment: str = None, disabled=False):
        self.address = IPAddress(address)
        if network:
            self.network = IPAddress(network)
        self.interface = interface
        self.comment = comment
        command = f'/ip address add address="{self.address}" interface="{interface}"'
        command += f' network="{self.network}"' if network else ''
        command += f' comment="{self.comment}"' if comment else ''
        command += f' disabled="yes"' if disabled else ''

        result = self.connection.send_command(command)
        if result:
            raise RouterError(result)
        logging.info(f"IP address '{self.address}' added to interface '{self.interface}'")
        return self

    def set(self, find_by: dict, address: str = None, interface: str = None, network: str = None, comment: str = None):
        self._checking_find_by_field(find_by)
        find = '[find'
        for k, v in find_by.items():
            find += f' {k}="{v}"'
        find += ']'
        command = f'/ip address set {find}'
        if address:
            self.address = IPAddress(address)
            command += f' address="{self.address}"'
        if interface:
            self.interface = interface
            command += f' interface="{self.interface}"'
        if network:
            self.network = IPAddress(network)
            command += f' network="{self.network}"'
        if comment:
            self.comment = comment
            command += f' comment="{self.comment}"'
        print(command)
        print(self.connection.send_command(command))
        return self

    def get_all(self) -> list:
        command = '/ip address print detail'
        result = self.connection.send_command(command)
        pattern = re.compile(r'\s*(\d+)\s+([DIX]?)\s*(?:\s*;;; (.*?))?\s*address=([0-9./]+)\s+network=([0-9.]+)\s+interface=([^\s]+)')
        addresses_string = pattern.findall(result)

        addresses: list[Address] = []
        for _address in addresses_string:
            _index, flag, comment, address, network, interface = _address
            addresses.append(self.__create_an_object(_index, flag, comment, address, network, interface))
        return addresses

    def get_only(self, find_by: dict):
        self._checking_find_by_field(find_by)
        command = '/ip address print detail where '
        for k, v in find_by.items():
            command += f'{k}="{v}" '
        result = self.connection.send_command(command)
        pattern = re.compile(
            r'\s*(\d+)\s+([DIX]?)\s*(?:\s*;;; (.*?))?\s*address=([0-9./]+)\s+network=([0-9.]+)\s+interface=([^\s]+)')
        try:
            address_ = pattern.findall(result)[0]
        except IndexError:
            raise InvalidSearchAttribute('Not find')
        address = self.__create_an_object(*address_)
        return address

    def print_all(self) -> str:
        addresses = self.get_all()
        text = ''
        for address in addresses:
            text += f'\n{address}'
        logging.info(text)
        return text

    def __create_an_object(self, _index, flag, comment, address, network, interface):
        ip_address = Address(connection=self.connection)
        ip_address.address = IPAddress(address)
        ip_address.network = IPAddress(network)
        ip_address.interface = interface
        ip_address.__number = int(_index)
        ip_address.flags = flag
        if flag == 'X':
            ip_address.disabled = True
        if comment:
            ip_address.comment = comment
        return ip_address

    def __str__(self):
        st = f'{self.__number} ' if self.__number is not None else ''
        st += f'{self.flags} address={self.address} network={self.network} interface={self.interface}'
        if self.comment:
            st += f' comment={self.comment}'
        return st


class Ip:
    def __init__(self, connection):
        self.connection = connection

    @property
    def address(self):
        address = Address(connection=self.connection)
        return address



