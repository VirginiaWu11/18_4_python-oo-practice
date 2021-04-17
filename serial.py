"""Python serial number generator."""

# from _typeshed import StrPath
from os import stat_result


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start
        self.inc = self.start-1
    def generate(self):
        "Increment by 1"
        self.inc += 1
        return self.inc
    def reset(self):
        "Reset number to start number"
        self.inc = self.start-1
        