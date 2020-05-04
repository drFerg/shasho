import socket
from struct import pack

CMD_ADDR = 0
CMD_SPEED = 1
CMD_POINT = 2

class EngineClient():
    """docstring for EngineClient"""
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET,     # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def setAddr(self, addr, newAddr):
      self.sock.sendto(pack('HHH', CMD_ADDR, addr, newAddr),
                      (self.addr, self.port))

    def setSpeed(self, addr, speed, direction):
        self.sock.sendto(pack('HHBB', CMD_SPEED, addr, speed, direction),
                         (self.addr, self.port))

    def setDirection(self, addr, direction):
        self.sock.sendto(pack('HHBB', CMD_SPEED, addr, 0, direction),
                         (self.addr, self.port))

    def switchPoint(self, point):
        self.sock.sendto(pack('HH', CMD_POINT, point),
                         (self.addr, self.port))