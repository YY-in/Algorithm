# -*- coding: utf-8 -*- 
# @Time : 2022/7/7 17:27 
# @Author : infinity-penguin
# @File : 删除排序数组中的重复项.py
from typing import List

from pyparsing import nums


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


if __name__ == '__main__':
    test = Solution()
    n = test.removeDuplicates([1, 2, 2, 3, 3, 4, 5, 5, 6])
    print(n)
