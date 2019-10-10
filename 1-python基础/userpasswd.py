
username = 'chenxiangming'
passwd = '12345678'
num = 0
while num < 4:
    name = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    if username == name and passwd == pwd:
        print('登录成功 welcome')
        break
    else:
        print('登录失败，你还有%d次机会'%(3-num))
        if (3-num) == 0:
            result = input('是否还想试试？yes')
            if result == 'yes':
                num = 0
                continue
            else:
                print('没有机会了')
                break
    num += 1
