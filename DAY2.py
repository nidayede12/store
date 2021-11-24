# 键盘输入
import random
# 随机生成数字（开始int 结束int）
lsp=5000
c=0
while True:
     Ran=random.randint(1,2)
     num=input("请输入数字")
     num=int(num)
     if num ==Ran:
         print("恭喜，猜对了")
         lsp=lsp+300
         print("当前余额"+str(lsp))
     else:
         if num>Ran:
             print("有点大")
         if num<Ran:
             print("有点小")
         lsp=lsp-100
         c=c+1
         if c==5:
             break
         print("抱歉，猜错了")
         print("当前余额"+str(lsp))


