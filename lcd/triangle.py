from webai import webai
import image

img = image.Image()

img.draw_line(10, 10, 100, 100)
img.draw_line(100, 100, 100, 10)
img.draw_line(100, 10, 10, 10)
webai.show(img=img)