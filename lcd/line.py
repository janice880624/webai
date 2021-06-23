from webai import webai
import image

img = image.Image()

img.draw_line(10, 10, 100, 100)
webai.show(img=img)