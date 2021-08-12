for i in range(0, 361, 2):                                          # 0,2,4,6,...,360
  webai.img = webai.res.loadImg('photo.jpg')                      # 載入開發板中的圖片成為Image物件
  webai.img.rotation_corr(y_rotation=i, x_translation=0, zoom=1)    # 圖像3D變形
  webai.show(img=webai.img)                                       # 圖像顯示在LCD