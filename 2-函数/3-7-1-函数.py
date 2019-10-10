# a = 1
# def func():
#     print(a)
# func()
# a = 1
# def func():
#     global a
#     a += 1
# func()
# # print(a)
# def func():
#     a = 12
#     b = 20
#     print(locals())
#     print(globals())
#
# func()
a = 1
def func():
    a = 2
    return a

print(func())
