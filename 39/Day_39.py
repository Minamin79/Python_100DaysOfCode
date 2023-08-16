import pyqrcode
from pyqrcode import QRCode


url = pyqrcode.create('https://github.com/Minamin79') 
url.svg('the_QRCode.svg', scale=8)