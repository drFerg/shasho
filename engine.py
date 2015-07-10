import crazyradio
from struct import pack


class Engine():
    """Communicates with dcc control box via nrf24 using a usb crazyradio"""
    def __init__(self):
        self.cr = crazyradio.Crazyradio()

    def setSpeed(self, address, speed, direction):
        print self.send(pack('HBB', address, speed, direction))

    def send(self, data):
        print self.cr.send_packet(data).ack
