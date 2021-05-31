# Convert image into black and white
# pip install Pillow

import os
from PIL import Image
os.chdir("E://")
img = Image.open("divu.JPG")
img.show()
blackANDwhite = img.convert("L")
# blackANDwhite.save("bw_divu.JPG")
blackANDwhite.show()
