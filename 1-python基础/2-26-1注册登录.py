username = input('请输入你要注册的用户名：')
password = input('请输入你要注册账号的密码：')
with open('list_of_info',mode='w',encoding='utf-8') as f:
    f.write('{}\n{}'.format(username,password))
print('注册成功')

i = 0
lis = []
while i < 3:
    print('登录')
    uname = input('请输入你的用户名')
    passwd =input('请输入你的密码')
    with open('list_of_info', mode='r', encoding='utf-8') as f1:
        for line in f1:
            lis.append(line)
    if uname == lis[0].strip() and passwd == lis[1].strip():
        print('登录成功：')
        break
    else:
        print('账号或密码错误')
    i += 1
