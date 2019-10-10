'''
a = "运维工程师"
b = "我们需要学习开发能力"
c = 2019
d = 100.00
e = "1234567qwertyu098765"
f = e[0:3]
g = e.replace('1','6')

print(f + g)
print(e.find('q'))

print('%d%s'%(c,b) )
'''
'''
c = "l,u,k,y=c=x=m"
clist = c.split(',','=') # 以逗号分隔l,u,k,y并保存列表中
for value in clist:  # for循环输出列表值
    print(value)

a = "c,x,m,=l=u=k=y"
import re
re.split(',|=',a)

flag = False
name = 'pyton'
if name == 'python':
#    flag = True
    print("Welcome back! ")
else:
    print(name)
str = "2019python"
print(str[:])
print(str[::-1])
print(str[-3:-1])
print(str[::2])
#截取
'''
"""
flag = False
name = 'cxm'
if name == 'cwwwxm':
    flag = True
    print('你好'+name)
else:
    print('名字是：'+name)
#if循环
"""
'''
#whlie循环语句
user_count = 0
while(user_count < 10):
    print('useradd -s /sbin/nologin',"newuser"+str(user_count))
    user_count = user_count + 1
'''
'''
#跳过此次循环continue
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6、8、10
'''
'''
#跳出循环break
i = 4
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
'''

