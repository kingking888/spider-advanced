# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# # 1.某互联网公司两位技术总监（甲、乙）去吃饭，坐在一家饭店靠近街道的窗口座位吃饭，在等待上菜的过程中，闲极无聊，甲向乙出了一道猜三个女儿年龄的题目。
# # 甲：我有3个女儿，3人年龄之积等于36；
# # 乙：猜不出来；
# # 甲：二女儿和三女儿年龄之和比大女儿大；
# # 乙：还是无法确定；
# # 甲：我的大女儿叫乔曼。
# # 乙：哦，我知道了。
# # 请问，甲的3个女儿年龄各是多少？用python代码实现
# for x in range(1, 36):
#     for y in range(1, 36):
#         if 36 % (x * y) == 0:
#             z = int(36 / x / y)
#             if y + z > x:
#                 if x > y >= z:
#                     print(x, y, z)

# # 2.字典m = {'a': 1, 'b': 2, 'c': 3},请用代码完成key和value的交换
# m = {'a': 1, 'b': 2, 'c': 3}
# m_new = {v: k for k, v in m.items()}
# print(m_new)

# # 3.假设给定列表number =[2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]，求出列表中正整数的平均值
# number = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
# print(sum(list(i for i in number if i > 0)) / len(list(i for i in number if i > 0)))

# # 5.假设有如下两个 list：a = ['a', 'b', 'c', 'd', 'e']，b = [1, 2, 3, 4, 5]，将 a 中的元素作为 key，b 中元素作为 value，将 a，b 合并为字典
# a = ['a', 'b', 'c', 'd', 'e']
# b = [1, 2, 3, 4, 5]
# dic = dict(zip(a, b))
# print(dic)
