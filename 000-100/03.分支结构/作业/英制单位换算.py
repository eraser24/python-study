"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: eraser
"""

long = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (long, long / 2.54))
elif unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (long, long * 2.54))
else:
    print('请输入正确的单位 “厘米，cm，英寸，in”')
