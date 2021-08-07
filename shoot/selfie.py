def click(name, state):                     #定義函數 
  if name == 'btnL' and state == 1:       #如果按下L按鈕，
    webai.img.save('photo.jpg')         #儲存照片
      
webai.addBtnListener(click)                 #偵測開發板按鈕

while True:
  if webai.btnR.btn.value() == 0:         #如果R按鈕被按下
    webai.show(file = 'photo.jpg')      #顯示已儲存的照片
  else:                                   #否則
    webai.img = webai.snapshot()        #從鏡頭取得一張圖像
    webai.show(img = webai.img)         #圖像顯示在LCD