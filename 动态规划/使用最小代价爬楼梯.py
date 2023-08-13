# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

# 请你计算并返回达到楼梯顶部的最低花费。

def fun(cost):
    n = len(cost)
    # min cost i 表示爬到顶部为i需要花费的最少费用
    min_cost = [0 for i in range(n+1)]
    min_cost[2] = min(cost[0], cost[1])
    for i in range(3, n+1):
        min_cost[i] = min(min_cost[i-2]+cost[i-2], min_cost[i-1]+cost[i-1])
    return min_cost[-1]

print(fun([10, 15, 20]))

 