
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # 如果当前价格比前一天高，计算差值并加入利润
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def leetcode(prices):

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

if __name__ == "__main__":
    # 示例测试
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 输出 7
    print(maxProfit([1, 2, 3, 4, 5]))      # 输出 4
    print(maxProfit([7, 6, 4, 3, 1]))      # 输出 0
