# -*- coding: utf-8 -*-
import math
import random
import sys


def randBonus(total, num):
    print(total, num)
    if num < 1:
        return
    if num == 1:
        print('第%d个人得到的红包金额为:%.2f' % (num, total))
    # 开始发红包
    res = []
    i = 1
    while num > 1:
        min = 1
        max = total/num * 2
        random_money = math.floor(max * random.random() * 100)/100
        random_money = min if random_money < min else random_money
        print('第%d个人发的红包金额为：%.2f' % (i, random_money))
        total = total - random_money
        res.append(random_money)
        i += 1
        num -= 1
    res.append(round(total, 2))
    print('第%d个人发的红包金额为：%.2f' % (i, total))
    print('总金额为%d' % sum(res))


if __name__ == '__main__':
    randBonus(100, 10)

