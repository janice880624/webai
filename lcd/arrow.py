# draw_arrow(x1, y1, x2, y2, color, thickness=1)
# draw_arrow(起點 x 座標, 起點 y 座標, 終點 x 座標, 終點 y 座標, 顏色, 寬度)

webai.clear() 
webai.img = image.Image()
webai.img.draw_arrow(10, 10, 150, 150)
webai.show(img=webai.img)