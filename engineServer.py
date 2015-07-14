import socket
import sys
import getopt
from engine import Engine
from struct import unpack


class EngineServer():
    """docstring for EngineServer"""
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET,     # IPV4
                                  socket.SOCK_DGRAM)  # UDP
        try:
            self.sock.bind((addr, port))
        except Exception as msg:
            print "Error binding socket on {0}:{1} - {2}".format(addr, port, msg)
            sys.exit(2)

        self.engine = Engine()
        print "Started engine server on {0}:{1}".format(addr, port)

    def listen(self):
        while True:
            data, addr = self.sock.recvfrom(6)
            cmd, addr, speed, direction = unpack('BHBB', data)
            print "Received {0} command for addr {1}".format(cmd, addr)
            self.engine.send(data)


if __name__ == "__main__":
    addr = "127.0.0.1"
    port = 5005

    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:p:h",
                                   ["address=", "port=", "help"])
    except Exception:
        print "-a 127.0.0.1 -p 5005"
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-a", "--address"):
            addr = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-h", "--help"):
            print "-a 127.0.0.1 -p 5005"

    e = EngineServer(addr, port)
    e.listen()
