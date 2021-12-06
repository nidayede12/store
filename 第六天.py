kali={"12345678":{"username":"小王","pwd":123456,"country":"中国","province":"陕西","city":"西安","street":"雁塔","door":1009,"money":10},
      "87654321":{"username":"小八","pwd":123456,"country":"中国","province":"陕西","city":"西安","street":"雁塔","door":1009,"money":20}}
from random import randint
# import money as money
# import username as username

money=0
kali_name="中国工商银行"

def jinruxintong():
  while True:
     print('****************\n'
          '*  中国工商银行  *\n'
          '****************\n'
          '1.开户         *\n'
          '2.存钱         *\n'
          '3.取钱         *\n'
          '4.转账         *\n'
          '5.查询         *\n'
          '6.Bye!         *\n'
          '****************\n')  # 界面显示
     x = int(input("请输入您需要的业务"))
     if x == 1:
        print("开户")
        useradd()
     elif x == 2:
        print("存钱 ")
        cmoney()
     elif x == 3:
        print("取钱")
        take()
     elif x == 4:
        print("转账")
        debit()
     elif x == 5:
        print("查询")
        zat()
     elif x == 6:
        print("Bye")
     else:
       print("输入信息有误")

def useradd():#添加账户
  while True:
        account=randint(10000000,99999999)#账户
        username=input("请输入用户名")#姓名
        pwd=input("请输入密码")#密码
        if pwd.isdigit() and len(pwd)==6:
            pwd = int(pwd)
        country=input("请输入您所在的国家\t\t")#地区需要添加\t\t表示一个tab，
        province=input("请输入您所在的省份\t\t")#省份
        city=input("请输入您所在的城市\t\t")#城市
        street=input("请输入您所在的街道\t\t")#街道
        door=input("请输入您所在的门牌号\t\t")#门牌
        gift=kaliadd(account,username,pwd,country,province,city,street,door,)#加入useradd内的全部数据
        if gift==1:
            print("开户成功")

            info='''
            --------工商银行--------
            1.账号：%s
            2.姓名：%s
            3.密码：%s
            4.国家：%s
            5.省份：%s
            6.城市：%s
            7.街道：%s
            8.门牌号：%s
            9.余额：%s
            '''
            print(info%(account,username,pwd,country,province,city,street,door,money))
            break
        elif gift==2:
            print("请使用其他用户")
        elif gift==3:
            print("数据库已满")


def kaliadd(account,username,pwd,country,province,city,street,door,): #加入useradd内的全部数据
        if account in kali:
            return 2
        if len(kali) >100:
            return 3
        kali[account]={
            "account":account,#从useradd的account获取的随机数
            "username":username,
            "pwd":pwd,
            "country":country,
            "province":province,
            "city":city,
            "street":street,
            "door":door,
            "kali_name":kali_name,
            "money":0
        }
        return 1
#存款
def cmoney():  # 新储户的开户功能
        print(kali)
        account = input("请输入账号")
        money=int(input("请输入存款金额"))
        if account in kali.keys():
            print("成功")
            money=money+kali[account]["money"]
            # print(money+kali[account]["money"])
        else:
            print("失败")

# 取款
def take():#取款函数
    print(kali)
    account=input("请输入账号")
    pwd=input("请输入密码")
    money=input("请输入取款金额")
    if account in kali.keys():
        print("成功")
    elif pwd in kali.keys():
        print("成功")
        money=kali[account]['money']-money
        # print(kali[account]['money']-money)
    else:
        print("失败")
#转账
def debit():
    account=input("转入的")
    debit=input("转出的")
    pwd=input("转出的密码")
    money=input("转出金额")
    # gift=debit1(account,debit,pwd,money)
    if account in kali.keys():
        print("转账成功")
    elif pwd in kali.keys():
        print("密码输入错误")
    elif debit in kali.keys():
        print("账号不存在")


def debit1(account,debit,pwd,money):
    if debit in kali.keys() and debit in kali.keys():
        if pwd == kali[debit][pwd]:
            if money <= kali[debit][money]:
                kali[account][money]=kali[account]["money"]+money
                kali[debit][money]=kali[debit]["money"]-money
            else:
                return 1
        else:
            return 2
    else:
        return 3
#查询
def zat():
    account = input("查询的账户")
    pwd = int(input("密码"))
    gift = zat1(account,pwd)
    if gift==1:
        print("查询成功")
        info ='''
        ---------工商银行-------
            1.账号：%s
            2.姓名：%s
            3.密码：%s
            4.国家：%s
            5.省份：%s
            6.城市：%s
            7.街道：%s
            8.门牌号：%s
            9.余额：%s
        ----------------------
        '''
        print(info%(account,kali[account]["username"],kali[account]['pwd'],kali[account]["country"],kali[account]["province"],kali[account]["city"],kali[account]["street"],kali[account]["door"],kali[account]['money']))
    if gift==2:
        print("密码错误")
    if gift==3:
        print("账号不存在")
def zat1(account,pwd):
    if account in kali.keys():
        if pwd ==kali[account]["pwd"]:
            return 1
        else:
            return 2
    else:
        return 3

jinruxintong()




