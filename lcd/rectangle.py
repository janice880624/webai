from webai import webai
import image

img = image.Image()

img.draw_rectangle(10, 10, 300, 220)

webai.show(img=img)