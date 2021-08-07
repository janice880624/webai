webai.img = image.Image()
webai.clear()

#臉
webai.img.draw_ellipse(160, 140, 145, 130, 0, (30, 144, 255), fill=True)
webai.img.draw_ellipse(160, 160, 120, 120, 0, (255, 255, 255), fill=True)

#眼睛
webai.img.draw_ellipse(120, 60, 30, 40, -20, (0, 0, 0), fill=True)
webai.img.draw_ellipse(120, 60, 27, 37, -20, (255, 255, 255), fill=True)
webai.img.draw_ellipse(130, 60, 15, 20, -10, (0, 0, 0), fill=True)
webai.img.draw_circle(133, 55, 8, (255, 255, 255), fill=True)

webai.img.draw_ellipse(200, 60, 30, 40, 20, (0, 0, 0), fill=True)
webai.img.draw_ellipse(200, 60, 27, 37, 20, (255, 255, 255), fill=True)
webai.img.draw_ellipse(190, 60, 15, 20, 10, (0, 0, 0), fill=True)
webai.img.draw_circle(187, 55, 8, (255, 255, 255), fill=True)


#嘴巴
webai.img.draw_ellipse(160, 180, 100, 50, 0, (0, 0, 0), thickness=3)
webai.img.draw_rectangle(57, 127, 210, 50, (255, 255, 255), fill=True)

#鼻子
webai.img.draw_ellipse(160, 110, 25, 15, 0, (255, 0, 0), fill=True)
webai.img.draw_line(160, 125, 160, 230, (0, 0, 0), 3)

#鬍鬚
webai.img.draw_line(180, 185, 240, 200, (0, 0, 0), 3)
webai.img.draw_line(180, 165, 240, 165, (0, 0, 0), 3)
webai.img.draw_line(180, 145, 240, 125, (0, 0, 0), 3)

webai.img.draw_line(140, 185, 80, 200, (0, 0, 0), 3)
webai.img.draw_line(140, 165, 80, 165, (0, 0, 0), 3)
webai.img.draw_line(140, 145, 80, 125, (0, 0, 0), 3)

webai.show(img=webai.img)
