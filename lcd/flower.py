# 偏移量
j = 20

webai.clear()
webai.img = image.Image()

# 莖
webai.img.draw_line(160, 123-j, 160, 240, (139, 71, 38), 10)

# 葉子
webai.img.draw_ellipse(190, 205, 15, 37, 50, (0, 205, 0), fill=True)
webai.img.draw_ellipse(130, 190, 15, 37, 130, (0, 205, 0), fill=True)

# 花瓣
for i in range(0, 360, 30):
  webai.img.draw_ellipse(160, 120-j, 20, 80, i+15, (255, 255, 0), fill=True)

# 花中間的圓圈
webai.img.draw_circle(160, 120-j, 55, fill=True)
webai.img.draw_circle(160, 120-j, 52, (205, 149, 12), fill=True)

# 花中間的個子
webai.img.draw_line(160, 80-j, 200, 120-j, (0, 0, 0), 3)
webai.img.draw_line(145, 85-j, 195, 135-j, (0, 0, 0), 3)
webai.img.draw_line(130, 90-j, 190, 150-j, (0, 0, 0), 3)
webai.img.draw_line(125, 105-j, 175, 155-j, (0, 0, 0), 3)
webai.img.draw_line(120, 120-j, 160, 160-j, (0, 0, 0), 3)

webai.img.draw_line(145, 155-j, 195, 105-j, (0, 0, 0), 3)
webai.img.draw_line(175, 85-j, 125, 135-j, (0, 0, 0), 3)
webai.img.draw_line(190, 90-j, 130, 150-j, (0, 0, 0), 3)
webai.img.draw_line(120, 120-j, 160, 80-j, (0, 0, 0), 3)
webai.img.draw_line(160, 160-j, 200, 120-j, (0, 0, 0), 3)

# 顯示照片
webai.show(img=webai.img)
        

