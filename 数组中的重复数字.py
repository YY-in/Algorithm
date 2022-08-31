# -*- coding: utf-8 -*-
# @Time : 2022/8/30 00:04
# @Author : infinity-penguin
# @File : 数组中的重复数字.py
# @Dec : 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
#        数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
#        请找出数组中任意一个重复的数字。
# @Input : 输入：[2, 3, 1, 0, 2, 5, 3]
# @Output：2 或 3
from typing import List
import time

"""
这道题考察沟通能力，先询问时间/空间需求
O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n)
"""


def cost_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} cost time:{time.perf_counter() - t:.8f} s')
        return result

    return fun


class Solution:
    """
    双指针解法，速度较慢，运行超时
    时间：O(n^2)
    空间：O(1)
    """

    def findRepeatNumber1(self, nums: List[int]) -> int:
        for j in range(0, len(nums) - 1, 1):
            for i in range(len(nums) - 1, j, -1):
                if nums[i] == nums[j]:
                    return nums[i]

    """
    先排序，然后看相邻元素是否有相同，又直接return
    时间：O(nlogn)
    空间：O(1)
    """

    def findRepeatNumber2(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]

    def findRepeatNumber3(self, nums: List[int]) -> int:
        repeatDict = {}
        for num in nums:
        if num not in repeatDict:
            repeatDict[num] = 1
        else:
            return num


class Test:
    a = [2, 3, 1, 0, 2, 5, 3]
    solution = Solution()

    @cost_time
    def test1(self):
        print(Test.solution.findRepeatNumber1(Test.a))

    @cost_time
    def test2(self):
        print(Test.solution.findRepeatNumber2(Test.a))


if __name__ == "__main__":
    test = Test()
    test.test1()
    test.test2()
