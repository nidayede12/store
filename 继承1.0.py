# class person:
#     name = ""#姓名
#     age =0#年龄
#     def setname(self,name):
#         if name =="":
#             print("名字不能为空")
#         else:
#             self.__name = name
#     def person(self,age):
#         if age<0:
#             print("年龄输入非法")
#         else:
#             self.__age=age
#     def show(self):
#       print("我叫",self.name,"今年",self.age,"。")
# class cook(person):#厨师
#      make=""#炒菜
#      def cook(self):
#          super().show()
#          print("正在",self.make)
# class apprentice(cook):#学徒
#      steam = ""
#      def apprentice(self):
#          super().cook()
#          print("也会",self.steam)
#
# z=apprentice()
# z.name="暴龙战士"
# z.age=24
# z.make="蒸饭"
# z.steam="炒菜"
# z.apprentice()






class person:
    name = ""
    age = 0
    gender=""
    work = ""

    def setname(self,name):
        if name =="":
            print("必填项")
        else:
            self.name=name
    def getname(self):
        return  self.name
    def setage(self,age):
        if age >0 or age<200:
            print("输入非法")
        else:
            self.age=age
    def getage(self):
        return  self.age
    def setgebder(self,gender):
        if gender !="男" and gender !="女":
            print("你的性别")
        else:
            self.gender=gender
    def getgender(self):
        return self.gender

    def swork(self):
        print(self.name,"正在",self.work)

    def shuo(self):
        print("我的名字",self.getname(),"，年龄",self.getage(),"我是",self.getgender(),)
class xinperson(person):
    schoolhao = 0
    def xinschool(self):
        super().shuo()
        print(self.getname(),"正在学习",",喜欢唱歌")

z=xinperson()
z.name="大桥"
z.age=26
z.gender="男"
z.work="dyouxi"
z.swork()
z.xinschool()

