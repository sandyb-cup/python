# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Example:
    def __init__(self,arr1, arr2):
        # 一定要加list转换一下 因为生成器只能使用一次
        self.list_1 = list(map(int, arr1))
        self.list_2 = list(map(int, arr2))
    def list_map(self):
        # 将多个变量进行返回 默认会把多个变量变成一个元组
        return self.list_1, self.list_2

    # 逆序输出两个列表
    def list_map_sort(self):
        return sorted(self.list1, reverse=True), sorted(self.list_2, reverse=True)

    # 列表求和
    def list_max(self):
        return sum(self.list_1), sum(self.list_2)

    # 返回偶数
    def list_fliter(self):
        #
        return filter(lambda x:x % 2 ==0, self.list_1), filter(lambda x:x % 2 == 0)
    # 将两个列表合并
    def list_zip(self):
        return list(zip(self.list_1, self.list_2))
    # 两个合并的列表输出一个字典
    def list_dict(self):
        return dict(self.list_zip())

    @property
    def list_1_set(self):
        return self .list_1
    @list_1_set.setter
    def list_1_set(self, arr):
        self.list_1 = arr
        return self.list_1


e = Example(['1','2','3','4'], '5678')
arr1, arr2 = e.list_map()
print(arr1)
print(arr2)
e.list_1_set = [0,0,0,0]
print(e.list_1_set)

