# dict_dic= {"k1":"v1","k2":"v2","k3":"v3"}
# dict_dic.update({"k4":"v4"})
# for dict in dict_dic:
#     print(dict)
# for dic in dict_dic:
#     print(dict_dic[dic])

#任务二
# key_value={"苹果":32.8,"香蕉":22,"葡萄":15.5}
# print(key_value)
# Friuts = {"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":15.8}#水果单价
# info={
#     '小明':{
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':0},
#     '小刚':{
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money':0}
# }
# for i in info['小明']['fruits']:
#      y=Friuts[i]*info['小明']['fruits'][i]
#      info['小明']['money']+=y
# print("小明的水果价格为",info['小明']['money'])
# for j in info['小刚']['fruits']:
#      x=Friuts[j]*info['小刚']['fruits'][j]
#      info['小刚']['money']+=x
# print("小刚的水果价格为",info['小刚']['money'])


#任务三有问题，待修改
# dict={21:3,
#       56:9,
#       10:3}
# print(list(dict.items()))
# dict ={}
# for i in dict:
# 	dict.update({i:dict.count(i)})
# print(dict)
# from collections import Counter
# x = Counter(dict)
# print(x)


#任务四有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# Trad=['姓名','年龄','性别','编号','任职公司','薪资','部门编号']
# #角标    0     1      2     3       4        5       6
# names = ({"姓名":'刘备',"年龄":56,"性别":'男',"编号":106,"任职公司":'MIB',"薪资":500 ,"部门编号":50},
#          {"姓名":'大乔',"年龄":19,"性别":"女","编号":230,"任职公司":"微软","薪资": 501 ,"部门编号":60},
#          {"姓名":'小乔',"年龄":19, "性别":"女","编号": 210, "任职公司":"Oracle","薪资": 600, "部门编号":60},
#          {"姓名":'张飞', "年龄":45,"性别": "男","编号":230,"任职公司":"Tencent","薪资":700 ,"部门编号":10},)
# print(names)
