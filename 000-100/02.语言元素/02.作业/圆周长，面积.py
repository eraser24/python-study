"""
练习2：输入圆的半径计算,计算周长和面积。
"""
import math

r = float(input('请输入圆的半径'))

zc = 2 * math.pi * r
mj = math.pi * r * r

print('圆的周长为: %f'  % zc)
print('圆的面积为: %f'  % mj)
print(math.pi)