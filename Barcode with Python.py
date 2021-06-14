# pip install pyqrcode


import pyqrcode
import png
from pyqrcode import QRCode

# String which represent the QR code
s = "http://www.codewithdivu.ml/"

# General QR code
url = pyqrcode.create(s)

# Create and save the png file naming ".png"
url.svg("eduyear.jpeg", scale=8)

url.png('myqr.png', scale = 6)