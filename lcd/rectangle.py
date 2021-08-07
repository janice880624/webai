# draw_rectangle(x, y, w, h, color, thickness=1, fill=False)
# draw_rectangle(左上角 x 座標, 左上角 y 座標, 寬度, 高度, 顏色, 寬度, 是否填充)

webai.img = image.Image()
webai.img.draw_rectangle(10, 10, 300, 220, thickness=250)
webai.show(img=webai.img)