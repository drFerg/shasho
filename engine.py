import crazyradio

class Engine():
    """Communicates with dcc control box via nrf24 using a usb crazyradio"""
    def __init__(self):
        self.cr = crazyradio.Crazyradio()

    def send(self, data):
        print self.cr.send_packet(data).ack
