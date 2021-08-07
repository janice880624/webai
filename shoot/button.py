def click(name, state):        # 定義函數 
  print(name, state)         # name='btnL'或'btnR'，state=1:按下, 2:放開, 3:長按

webai.addBtnListener(click)    # 偵測開發板按鍵