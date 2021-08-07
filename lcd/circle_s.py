while True:
  for i in range(10, 100, 5):
    webai.clear()
    webai.img.draw_circle(160, 120, i)
    webai.show(img=webai.img)