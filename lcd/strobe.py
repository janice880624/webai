webai.img = image.Image()                                           #宣告空的圖片物件

def Flashing(Light):                                                #定義函數(亮哪個燈)
  for i in range(2):                                              #執行兩次亮燈與滅燈
    if('L' in Light):                                               #如果參數包含L畫左燈
      webai.img.draw_rectangle(0,80,140,80,(0,0,255),fill=True)
    if('R' in Light):                                               #如果參數包含R畫右燈
      webai.img.draw_rectangle(180,80,140,80,(255,0,0),fill=True)
    webai.show(img=webai.img)
    time.sleep(0.1)                                                 #短暫等待
    webai.img.clear()                                               #清除螢幕，滅燈
    webai.show(img=webai.img)
    time.sleep(0.1)                                                 #短暫等待

while True:                                                         #重複執行
  for i in range(4):                                                  #執行四次
    Flashing('L')                                                       #左燈閃兩下
    Flashing('R')                                                       #右燈閃兩下
    time.sleep(0.2)                                                     #短暫等待
  for i in range(3):                                                  #執行三次
    Flashing('LR')                                                      #兩個燈一起閃兩下
  time.sleep(0.2)    