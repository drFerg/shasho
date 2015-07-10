import socket
from struct import pack


class EngineClient():
    """docstring for EngineClient"""
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET,     # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def setSpeed(self, addr, speed, direction):
        self.sock.sendto(pack('HBB', addr, speed, direction),
                         (self.addr, self.port))

    def setDirection(self, addr, direction):
        self.sock.sendto(pack('HBB', addr, 0, direction),
                         (self.addr, self.port))
