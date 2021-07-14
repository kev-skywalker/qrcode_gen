import pyqrcode
from pyqrcode import QRCode


def generateQRcode(addr, filename):
    # Generate QR code
    url = pyqrcode.create(addr)
    # Create and save the png file
    url.png(filename, scale = 8)

print(url.terminal('red', 'white'))
