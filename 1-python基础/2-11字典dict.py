# dic1 = {
#     'name':['cxm','yly','love'],
#     'pu':{
#         'time':'2-11',
#         'money':7000,
#         'age':25
#     }
# }
# # dic1['age'] = 65
# # print(dic1)
# # dic1['name'].append(1,'hahah')
# # print(dic1)
#
# # print(dic1['pu'])
# #字典添加k-v
# dic1['pu']['aaa'] = 6
# print(dic1)

info = input('>>>')  #请输入
for i in info:
    if i.isalpha():
        info = info.replace(i,' ')
    l = info.split()
print(l)
print(len(l))

