from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./codes/test4.png')

result = decode(img)

print(result)