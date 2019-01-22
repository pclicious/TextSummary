from PIL import Image
from pytesseract import image_to_string

#myText = image_to_string(Image.open("tmp/test.jpg"),config='-psm 10')
myText = image_to_string(Image.open("phototest.tif"))
print(myText)