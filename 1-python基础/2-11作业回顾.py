'''
    有如下值li= [11,22,33,44,55,66,77,88,99,90]，
    将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''
li = [11,22,33,44,55,66,77,88,99]
dic1 = {}
greater = []    #大于66的所有值列表
less = []       #小于66的所有值列表
for i in li:
    if i > 66:
        greater.append(i)
    elif i < 66:
        less.append(i)
    elif i == 66:
        continue
dic1.setdefault('k1',greater)
dic1.setdefault('k2',less)
print(dic1)
