from webai import webai
import image

img = image.Image()

img.draw_circle(160, 120, 40)

webai.show(img=img)