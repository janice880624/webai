# draw_cross(x, y, color, size=5, thickness=1)
# draw_cross(x 座標, y 座標, 顏色, 大小, 寬度)

webai.clear() 
webai.img = image.Image()
webai.img.draw_string(100, 100, '哈囉', scale=2)
webai.show(img=webai.img)