while True:
  webai.img = webai.snapshot()  # 從鏡頭取得一張圖像
  webai.show(img = webai.img)   # 影像顯示在LCD  
  time.sleep(0.2)