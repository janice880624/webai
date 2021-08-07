# draw_ellipse(x, y, rx, ry, rotation, color, thickness=1, fill=False)
# draw_ellipse(圓心 x 座標, 圓心 y 座標, 寬度, 高度, 角度, 顏色, 寬度, 是否填充)

webai.img = image.Image()
webai.img.draw_ellipse(160, 120, 40, 80)
webai.show(img=webai.img)