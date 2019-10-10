'''
购物车
'''
li = [
    {'name':'苹果','price':10},
    {'name':'香蕉','price':20},
    {'name':'西瓜','price':30},
]   #物品列表及价格
shopping = {}   #购物车字典
print('欢迎光临')
money = input('你有多钱')
if money.isdigit() and int(money) > 0:
    flag = True
    while flag:
        for i,k in enumerate(li):   #遍历元素
            print('序号{}，商品{},价格{}'.format(i,k['name'],k['price']))
        choose = input('请输入要购买的商品序号')
        if choose.isdigit() and int(choose) < len(li):
            num = input('请输入您要购买的商品数量')
            if num.isdigit():
                if int(money) >= li[int(choose)]['price'] * int(num):
                    money = int(money) - li[int(choose)]['price'] * int(num)    #剩余金额
                    if li[int(choose)]['name'] in shopping:
                        shopping[li[int(choose)]['name']] = shopping[li[int(choose)]['name']] + int(num)    #有商品名，数量+
                    else:
                        shopping[li[int(choose)]['name']] = int(num)    #没有商品名，添加商品名、数量
                    print('购物车的商品有个{}，您的余额还剩{}'.format(shopping,money))
                else:
                    print('余额不足请充值')
                    break
        else:
            print('输入有误，请输入要购买的商品序号')
    else:
        print('没钱买个屁啊')