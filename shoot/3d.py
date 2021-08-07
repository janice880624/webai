webai.img = webai.res.loadImg('photo.jpg')                            #載入開發板中的圖片成為Image物件
webai.img.rotation_corr(y_rotation=25, x_translation=15, zoom=0.8)    #圖像3D變形
webai.show(img=webai.img) 