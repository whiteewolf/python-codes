import qrcode
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styledpil import StyledPilImage

text = input("What should the Qr Code return? : ")

img = qrcode.QRCode(version=1, box_size=10, border=5)
img.add_data(text)
img.make(fit=True)
img = img.make_image(image_factory= StyledPilImage,color_mask=RadialGradiantColorMask())

# you must change file name for every new qr code until i make a proper system
img.save('./codes/test4.png')

print('Qr Code has been made and saved to folder \'codes\'... ')