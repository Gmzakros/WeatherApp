from rembg import remove
from PIL import Image


i = input('enter the name of the file you want to remove: ')

s = input('save name for file: ')


inputImg = Image.open(".\\Assets\\" + i)
outputImg = remove(inputImg)
outputImg.save('.\\Assets\\' + s)

