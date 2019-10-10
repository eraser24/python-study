"""
输入年份如果是闰年输出True否则输出False

Version: 0.1
Author:eraser
"""

year = int(input('请输入年份：'))


judge = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
if judge:
    print('%d 年是闰年'% year)
else:
    print('%d 年不是闰年' % year)