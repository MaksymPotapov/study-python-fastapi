from abc import ABC, abstractmethod


class Print(ABC):
    @classmethod
    @abstractmethod
    def print(self):
        pass

class Scan(ABC):
    @classmethod
    @abstractmethod
    def scan(self):
        pass

class Copy(ABC):
    @classmethod
    @abstractmethod
    def copy(self):
        pass

class NetworkPrinter(Print, Scan, Copy):
    def print(self):
        print('Printing file with network printer...')

    def scan(self):
        print('Scanning paper with network printer...')

    def copy(self):
        print('Copying paper with network printer...')

class Printer(Print):
    def print(self):
        print('Printing file with printer...')

class Scanner(Scan):
    def scan(self):
        print('Scanning paper with scanner...')


network_printer = NetworkPrinter()
network_printer.print()
network_printer.scan()
network_printer.copy()
print('------------------------------------------')
printer = Printer()
printer.print()
print('------------------------------------------')
scanner = Scanner()
scanner.scan()