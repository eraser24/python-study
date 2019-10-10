"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: eraser
"""
print('请输入a,b,c三边长度，单位：cm')
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and c + b > a:
    print('此三角形周长为：%fcm' % (a + b +c))
    p = (a + b + c ) / 2
    print('此三角形面积为:%f 平方厘米' % ((p * (p - a) * (p - b) * (p - c)) ** 0.5))
else:
    print('不能构成三角形')
