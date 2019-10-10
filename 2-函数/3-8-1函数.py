# def max2(x,y):
#     m  = x if x>y else y
#     return m
#
# def max4(a,b,c,d):
#     res1 = max2(a,b)
#     res2 = max2(res1,c)
#     res3 = max2(res2,d)
#     return res3
# print(max4(23,-7,31,11))

# def f1():
#     a = 1
#     def f2():
#         print(a)
#     f2()
# f1()

# def f1():
#     a = 1
#     def f2():
#         nonlocal a
#         a = 2
#     f2()
#     print('a in f1 : ',a)
# f1()

# def func():
#     print('in func')
# f = func
# print(f)

# def f1():
#     print('f1')
# def f2():
#     print('f2')
# def f3():
#     print('f3')
# l = [f1,f2,f3]
# d = {'f1':f1,'f2':f2,'f3':f3}
# #调用
# l[0]()
# d['f2']()

def outer():
    def inner():
        print(a)




















