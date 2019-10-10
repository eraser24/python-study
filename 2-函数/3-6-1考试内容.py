# count = 0
# content = input('>>>')
# for i in range(len(content)):
#     if i % 2 == 1 and content[i].isdigit():
#         count += 1
# print(count)
# content = input('请输入内容：')
# content_list = content.split('+')
# # print(content_list)
# sum = 0
# for i in content_list:
#     sum = sum + int(i)
# print(sum)
user_list = []
board = ['张三','李小四','王二麻子']
flag = True
while flag:
    username = input('请输入名字：')
    if username.upper() == 'Q':
        break
    if username in board:
        username = username.replace(username,'*'*len(username))
    password = input('请输入密码：')
    user_list.append({'username':username,'password':password})
    print({'username':username,'password':password})
print(user_list)

