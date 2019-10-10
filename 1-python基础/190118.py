# #123456 8910
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         pass
#         # continue
#     else:
#         print(count)

# #1+.......100和
# a = 1
# b = 2
# while b <= 100:
#     a = a + b
#     b += 1
# print(a)
# #基数
# a = 1
# while a <=100:
#     if a % 2 == 0:
#         pass
#     else:
#         print(a)
#     a += 1
# 1-2+3-4+5····+99-100
# sum = 0
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         sum = sum - count
#         count += 1
#     else:
#         sum = sum + count
#         count += 1
# print(sum)

















li = [
    {'name':'苹果','price':10},
    {'name':'香蕉','price':20},
    {'name':'西瓜','price':30},
]
for i, k in enumerate(li):
    print('序号{}，商品{},价格{}'.format(i, k['name'], k['price']))
choose = input('请输入要购买的商品序号')
print(li[int(choose)]['price'])