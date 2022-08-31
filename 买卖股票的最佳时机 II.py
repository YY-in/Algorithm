# -*- coding: utf-8 -*- 
# @Time : 2022/7/7 18:14 
# @Author : infinity-penguin
# @File : 买卖股票的最佳时机 II.py
# @Dec  : 给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
#         在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#         返回 你能获得的 最大 利润。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] - prices[i] > 0)


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[2, 453, 23, 45, 5, 621, 12, 456, 423]))
