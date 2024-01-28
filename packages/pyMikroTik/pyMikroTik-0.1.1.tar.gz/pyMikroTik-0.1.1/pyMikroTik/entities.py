from .exceptions import IpAddressFormatError, InvalidSearchAttribute


class MTObject:
    def _checking_find_by_field(self, find_by: dict) -> bool:
        """Возращает True если все поля поиска существуют для данного объекта.
        Иначе генерируется исключение InvalidSearchAttribute"""
        if not isinstance(find_by, dict):
            raise ValueError("'find_by' must by 'dict'")
        attributes_ls = list(vars(self).keys())
        attributes_ls.remove('connection')
        attributes_ls.remove('flags')
        for field in find_by.keys():
            if field not in attributes_ls:
                raise InvalidSearchAttribute(f'The "{field}" attribute does not exist for the IP object. \n'
                                             f'Use only {attributes_ls}')
        return True


class IPAddress:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise ValueError('Object must be a string')
        self._value = value.strip()
        self.address = None
        self.mask = None
        self.checking_value()

    def checking_value(self):
        address_mask = self._value.split('/')
        try:
            if len(address_mask) > 2:
                raise ValueError
            address = address_mask[0].split('.')
            if len(address) != 4:
                raise ValueError
            for a in address:
                _ip = int(a)
                if _ip < 0 or _ip > 255:
                    raise ValueError
            self.address = address_mask[0]
            if len(address_mask) == 2:
                _mask = int(address_mask[1])
                if _mask < 1 or _mask > 32:
                    raise ValueError
                self.mask = str(address_mask[1])
        except ValueError:
            raise IpAddressFormatError('Invalid IP address format.\nExample: 192.168.32.15/24')

    def __str__(self):
        address = self.address
        if self.mask:
            address += f'/{self.mask}'
        return address


