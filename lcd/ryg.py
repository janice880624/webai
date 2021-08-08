i = (211, 211, 211)
j = (0, 0, 0)
k = 90
r = (255, 0, 0)
y = (255, 255, 0)
g = (0, 255, 0)
t = 2

webai.clear() 
webai.img = image.Image()

webai.img.draw_rectangle(10, 80, 300, 80, i, fill=True)
webai.img.draw_rectangle(20, 70, 280, 100, i, fill=True)
webai.img.draw_circle(20, 80, 10, i, fill=True)
webai.img.draw_circle(300, 80, 10, i, fill=True)
webai.img.draw_circle(20, 160, 10, i, fill=True)
webai.img.draw_circle(300, 160, 10, i, fill=True)

webai.img.draw_rectangle(20, 75, 280, 90, j, fill=True)
webai.img.draw_rectangle(15, 80, 290, 80, j, fill=True)
webai.img.draw_circle(20, 80, 5, j, fill=True)
webai.img.draw_circle(300, 80, 5, j, fill=True)
webai.img.draw_circle(20, 160, 5, j, fill=True)
webai.img.draw_circle(300, 160, 5, j, fill=True)

#webai.img.draw_circle(160-k, 120, 37, r, fill=True)
#webai.img.draw_circle(160, 120, 37, y, fill=True)
#webai.img.draw_circle(160+k, 120, 37, g, fill=True)

while True:
  webai.img.draw_circle(160-k, 120, 37, r, fill=True)
  webai.img.draw_circle(160, 120, 37, j, fill=True)
  webai.img.draw_circle(160+k, 120, 37, j, fill=True)
  webai.show(img=webai.img)
  time.sleep(2)
  
  webai.img.draw_circle(160-k, 120, 37, j, fill=True)
  webai.img.draw_circle(160, 120, 37, y, fill=True)
  webai.img.draw_circle(160+k, 120, 37, j, fill=True)
  webai.show(img=webai.img)
  time.sleep(2)
  
  webai.img.draw_circle(160-k, 120, 37, j, fill=True)
  webai.img.draw_circle(160, 120, 37, j, fill=True)
  webai.img.draw_circle(160+k, 120, 37, g, fill=True)
  webai.show(img=webai.img)
  time.sleep(2)


