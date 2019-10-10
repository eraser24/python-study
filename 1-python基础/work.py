# num = 1
# sum = 0
# while num < 100:
#     if num == 88:
#         num += 1
#         continue
#     else:
#         if num % 2 == 0:
#             sum = sum - num
#         else:
#             sum = sum + num
#     num += 1
# print(sum)
#

num = 0
j = -1
sum = 0
while num < 100:
    num += 1
    if num == 88:
        continue
    else:
        j = -j
        sum = sum + num * j
print(sum)
