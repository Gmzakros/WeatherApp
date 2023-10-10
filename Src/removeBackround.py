from rembg import remove
from PIL import Image
import os

dir = '.\\Assets'
for file in os.listdir(dir):
    f = os.path.join(dir, file)
    # checking if it is a file
    if os.path.isfile(f):
        inputImg = Image.open(f)
        outputImg = remove(inputImg)
        outputImg.save(f)






