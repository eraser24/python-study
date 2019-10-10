# f = open('文件操作',mode='rb')
# content = f.read()
# print(content)
# f.close()

# f = open('log',mode='wb')

# f.write('你是猴子派来的逗逼吗？'.encode('utf-8'))
# f.close()

#
# f = open('log',mode='a',encoding='utf-8')
# f.write('\n是的我是')
# f.close()

# f = open('log',mode='w+',encoding='utf-8')
# f.write('bbb')
# f.seek(0)
# print(f.read())
# f.close()

# f = open('log',mode='a+',encoding='utf-8')
# f.write('\n11111')
# f.seek(0)
# print(f.read())
# f.close()

f = open('log',mode='a+',encoding='utf-8')
f.write('123')
f.seek(f.tell()-3)
print(f.read())
f.close()








