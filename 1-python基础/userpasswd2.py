username = 'cxm'
passwd = '123'
i = 2
while i >= 0:
    name = input('输入用户名：')
    if username == name:
        pwd = input('请输入密码：')
        if i == 0:
            reinput = input('你已经没有机会了：如果继续请按y')
            if reinput == 'y':
                i = 2
            else:
                print('拜拜')
                break
        else:
            print('密码输入错误，请重新输入')
            print('你还有%s次机会'%(i))
            i -= 1
    else:
        if i == 0:
            reinput = input('你已经没有机会了：如果继续请按y')
            if reinput == 'y':
                i = 2
            else:
                print('拜拜')
                break
        else:
            print('用户名输入错误，请重新输入')
            print('你还有%s次机会'%(i))
            i -= 1
