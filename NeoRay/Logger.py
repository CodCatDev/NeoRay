#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev
#
#   NeoRay.Logger

import datetime

class _Logger:
    """
    Base logger class for all loggers (MainLogger, HttpLogger and etc)
    """
    __pattern__ = ""
    __name__ = "NeoRay"
    def log(self, message: str, **kwargs) -> None:
        """
        Log info to console with a pattern (pattern sets by logger type (MainLogger, HttpLogger and etc))

        Args:
            message (str): Message to log
            **kwargs: Additional arguments
        """
        level = "INFO"
        print(self.__pattern__.format(name=self.__name__, log=message, time=datetime.datetime.now().strftime("%H:%M:%S"), level=level, **kwargs))
    
    def error(self, message: str, **kwargs) -> None:
        """
        Log error to console with a pattern (pattern sets by logger type (MainLogger, HttpLogger and etc))

        Args:
            message (str): Message to log
            **kwargs: Additional arguments
        """
        level = "ERR"
        print(self.__pattern__.format(name=self.__name__, log=message, time=datetime.datetime.now().strftime("%H:%M:%S"), level=level, **kwargs))
    
    def warn(self, message: str, **kwargs) -> None:
        """
        Log warning to console with a pattern (pattern sets by logger type (MainLogger, HttpLogger and etc))

        Args:
            message (str): Message to log
            **kwargs: Additional arguments
        """
        level = "WARN"
        print(self.__pattern__.format(name=self.__name__, log=message, time=datetime.datetime.now().strftime("%H:%M:%S"), level=level, **kwargs))

class CustomLogger(_Logger):
    def __init__(self, pattern: str = "[{name}] [{time}] {level} {log}", name: str = "MyCustomLogger") -> None:
        """
        Custom logger for console

        Args:
            pattern (str): Pattern for logging
            name (str): Name of logger
        """
        self.__pattern__ = pattern
        self.__name__ = name

class MainLogger(_Logger):
    def __init__(self, name: str = "NeoRay") -> None:
        """
        Main logger for console
        """
        self.__name__ = name
        self.__pattern__ = "[ {name} ] ({level}) [{time}] - {log}"

class HttpLogger(_Logger):
    def __init__(self) -> None:
        """
        Http logger for console
        """
        self.__name__ = "NeoRay"
        self.__pattern__ = "[{requestType}] ({time}) - {log}"