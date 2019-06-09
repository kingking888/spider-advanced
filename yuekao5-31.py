# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# 1、有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那两位。
# import copy
#
#
# def baoshu(n):
#     list_zong = list(range(1, n + 1))
#     list_new = copy.deepcopy(list_zong)
#     flag = 0
#     while len(list_new) > 2:
#         for i in list_zong:
#             flag += 1
#             if flag == 3:
#                 list_new.remove(i)
#                 flag = 0
#         list_zong = copy.deepcopy(list_new)
#     return list_new
#
#
# if __name__ == '__main__':
#     print(baoshu(5))
#     print(baoshu(100))

# def who_remain(n):
#     lst = list(range(1, n + 1))
#     while len(lst) > 2:
#         before = lst[:2]
#         lst = lst[3:]
#         lst.extend(before)
#     return lst
# print(who_remain(100))


# 2、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222=24690(此时共有5个数相加，n=5)，几个数相加以及这个a是几都由控制台输入。设计程序，输入为n和a，输出结果

def sums(n, a):
    s = 0
    a_str = ''
    a = str(a)
    for i in range(n):
        a_str += a
        s += int(a_str)
    return s


if __name__ == '__main__':
    n = input('输入几个数相加:')
    a = input('输入哪个数相加:')
    print(sums(int(n), int(a)))
