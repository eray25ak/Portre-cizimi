from turtle import shape
from sketchpy import canvas
import cv2
im=cv2.imread('C:\\Users\\Eray\\Downloads\\WhatsApp Image 2023-12-06 at 22.58.06.jpeg')
print(im.shape)
obj=canvas.sketch_from_image('C:\\Users\Eray\\Downloads\\WhatsApp Image 2023-12-06 at 22.58.06.jpeg')
obj.draw(threshold=80)