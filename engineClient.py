import socket
from struct import pack

CMD_ADDR = 0
CMD_SPEED = 1


class EngineClient():
    """docstring for EngineClient"""
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET,     # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def setAddr(self, addr, newAddr):
      self.sock.sendto(pack('BHH', CMD_ADDR, addr, newAddr))

    def setSpeed(self, addr, speed, direction):
        self.sock.sendto(pack('BHBB', CMD_SPEED, addr, speed, direction),
                         (self.addr, self.port))

    def setDirection(self, addr, direction):
        self.sock.sendto(pack('BHBB', CMD_SPEED, addr, 0, direction),
                         (self.addr, self.port))
