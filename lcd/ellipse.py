from webai import webai
import image

img = image.Image()
webai.clear()

img.draw_ellipse(150, 150, 40, 80)

webai.show(img=img)