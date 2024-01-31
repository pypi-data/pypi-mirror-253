import collections
import warnings

import requests


class ApiError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IPX800V3:
    """Class representing the IPX800V3 and its "API".

    Attributes:
        outputs  the physical relays
        inputs  the physical inputs
    """

    def __init__(self, host:str, port : int = 80, username : str = "username", password : str = "password"):
        self.host = host
        self.port = port
        self.url = f"http://{self.host}:{self.port}"
        self.username = username
        self.password = password
        self.outputs = GenericSlice(self, Output, f"/api/xdevices.json", {"cmd": "20"})
        self.inputs = GenericSlice(self, Input, f"/api/xdevices.json", {"cmd": "10"})

    def ping(self) -> bool:
        """simple query to xdevices.json api and check value of return to ping the IPX"""
        response = self._request(url=f"/api/xdevices.json",params={})
        return isinstance(response, dict)

    def _request(self, url: str, params: dict, json : bool = True):
        # (bug) IPX4, key must be the first parameter otherwise some
        # calls don't return.
        # params.update({"key": self.api_key})
        auth = (self.username, self.password)
        r = requests.get(f"{self.url}{url}", auth=auth, params=params, timeout=2)
        r.raise_for_status()
        if json:
            content = r.json()
            product = content.pop("product", None)
            if product != "IPX800_V3":
                warnings.warn(f"Your device '{product}' might not be compatible")
            response = content
        else:
            response = True
        return response


class GenericSlice(collections.abc.Sequence):
    """Slice implementation for an iterable over GCE objects"""

    def __init__(self, ipx, gce_type, url, request_arg=None):
        self._ipx = ipx
        self._length = None
        self._type = gce_type
        self._rarg = request_arg
        self._url = url

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [
                self._type(self._ipx, k + 1)
                for k in range(key.start, key.stop, key.step)
            ]
        elif isinstance(key, int):
            if key < self.__len__():
                return self._type(self._ipx, key + 1)
            else:
                raise IndexError
        else:
            raise TypeError("Slice of 'int' is the only accepted range")

    def __len__(self):
        if self._length is None:
            self._length = len(self._ipx._request(url=self._url, params=self._rarg))
        return self._length


class BaseSwitch(IPX800V3):
    """Base class to abstract switch operations."""

    def __init__(self, ipx, prefix:str, id:int, name:str, cmd:str):
        super().__init__(host=ipx.host, port=ipx.port, username=ipx.username, password=ipx.password)
        self.id = id
        self._name = name
        self._cmd = cmd
        self._prefix = prefix

    @property
    def status(self) -> bool:
        """Return the current status."""
        params = {"cmd": self._cmd}
        response = self._request(url=f"/api/xdevices.json", params=params)
        return response[f"{self._prefix}{self.id}"] == 1

    def on(self) -> bool:
        """Turn on and return True if it was successful."""
        params = {f"set{self.id}": 1}
        self._request(url=f"/preset.htm", params=params, json=False)
        return True

    def off(self) -> bool:
        """Turn off and return True if it was successful."""
        params = {f"set{self.id}": 0}
        self._request(url=f"/preset.htm", params=params, json=False)
        return True
    
    def toggle(self) -> bool:
        """Toggle the output and return True if successful."""
        if self.status == 1:
            self.off()
        else:
            self.on()
        return True

    def __repr__(self) -> str:
        return f"<ipx800.{self._name} id={self.id}>"

    def __str__(self) -> str:
        return (
            f"[IPX800-{self._name}: id={self.id}, "
            f"status={'On' if self.status else 'Off'}]"
        )


class Output(BaseSwitch):
    """IPX800v3 output"""
    def __init__(self, ipx, id: int):
        super().__init__(ipx=ipx, prefix="OUT", id=id, name="output", cmd="20")

class Input(BaseSwitch):
    """ IPX800v3 input"""
    def __init__(self, ipx, id: int):
        super().__init__(ipx=ipx, prefix='IN', id=id, name="input", cmd="10")
    
    def on(self):
        raise NotImplementedError
    
    def off(self):
        raise NotImplementedError
    
    def toggle(self):
        raise NotImplementedError