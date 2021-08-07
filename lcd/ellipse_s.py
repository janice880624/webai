while True:
  for i in range(40, 80, 5):
    webai.clear()
    webai.img.draw_ellipse(160, 120, 40, i)
    webai.show(img=webai.img)
  for i in range(40, 80, 5):
    webai.clear()
    webai.img.draw_ellipse(160, 120, i, 40)
    webai.show(img=webai.img)