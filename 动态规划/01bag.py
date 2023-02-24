# 0 1 背包问题：
# 将不同重量和价值的物品放到背包里面；在背包的容量有限的情况下如何使地背包内的物品总价值最大

def test_bag(item_weights:list, item_values:list, bag_size:int):
    
    num = len(item_weights)
    dp = [0] * (bag_size+1) # dp数组下标表示容量，对应的值表示最大的物品价值
    for i in range(num):
        for j in range(bag_size, item_weights[i]-1, -1):
            dp[j] = max(dp[j], dp[j-item_weights[i]] + item_values[i])
    return dp

weight = [1, 3, 4, 6]
value = [15, 20, 30, 40]
bag_size = 11

dp = test_bag(weight, value, bag_size)
print(dp)