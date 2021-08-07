while True:
  webai.img = webai.snapshot()             #啟動鏡頭，拍照
  webai.img.cartoon(seed_threshold=0.2)    #卡通化濾波
  webai.show(img=webai.img)                #顯示圖片