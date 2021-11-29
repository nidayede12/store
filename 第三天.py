#任务二和任务一  求和
# x=0#求和
# y=1#循环
# c=0#比较求最大数
# while y<=12:
#    s=int(input("输入一个数字"))
#    x=x+s
#    print("第", y, "次生成数据的和为", x)
#    if s>c:
#       c=s
#    y=y+1
# print("最大值",c)
# print("平均数",x/y)



#任务三  随机数
# import random
# Ran=random.randint(50,150)
# print("随机数",Ran)

#任务四  三角形
# while True:
#  x=input("请输入第一条边")
#  x=int(x)
#  y=input("请输入第二条边")
#  y=int(y)
#  z=input("请输入第三条边")
#  z=int(z)
#  if (x>0,y>0,z>0):
#    if (x+y>z,x+z>y):
#     print("构成普通三角形")
#     if(x==y and x!=z) or (y==z and y!=x) or (z==x and y!=x):
#        print("构成等腰三角形")
#     if(x==z and x==y and y==z):
#         print("构成等边三角形")
#     if((x*x+y*y==z*z)or(x*x+z*z==y*y)or(y*y+z*z==x*x)):
#          print("构成直角三角形")


#任务五 数字对调
# A=15
# B=24
# while True:
#  s=input("请输入信息")
#  if (s=="+"):
#    print("a=",A)
#    print("b=",B)
#  if (s=="-"):
#    print("b=",B)
#    print("a=",A)

#任务六 登录系统
# z="root"
# s="admin"
# m=1
# z=input("请输入用户名")
# print("用户名输入错误")
# input("再次输入用户名")
# while m<=3:
#  if (z!="root"):
#   s=input("请输入密码")
#  if (z=="root"):
#    print("用户名输入正确")
#  if (s!="admin"):
#   print("密码输入错误")
#   m = m + 1
#  if(s=="admin"):
#   print("登陆成功，欢迎使用本系统")
#   break


#任务七 三角形
# for i in range(10):
#     for j in range(0, 10 - i):
#         print(end=" ")
#     for k in range(10 - i, 10):
#         print("*", end=" ")
#
#     print("")


#任务八 乘法口诀
# i=1#行控制
# while i<=9:
#     j = 1#列控制
#     while j<=i:
#         print("%dx%d=%d"%(i,j,i*j),end=' ')
#         j=j+1
#     print(' ')
#     i+=1
# print("乘法表倒叙打印:")
# for x in range(9,0,-1):
#     for y in range(x,0,-1):
#         print(f'{x}*{y}=' + str(x * y), end="\t")
#     print()

#任务九 青蛙爬井
# a = input('输入井口高度:')
# b = int(a) / 1
# if int(list(str(b))[-1]) > 1:
#     c = str(int(b)) + '1'
#     print('跳出井口的天数为:%s' % c)
# elif int(list(str(b))[-1]) == 0:
#     print('跳出井口的天数为:%s' % int(b))

# x=1
# y=0
# for i in range(1,21):
#     x*=i
#     y+=x
#     print(y)


