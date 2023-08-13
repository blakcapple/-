# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。
# 该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。
# 也就是： F(0) = 0，F(1) = 1 F(n) = F(n - 1) + F(n - 2)，其中 n > 1 给你n ，请计算 F(n) 。


def fun(n):
    if i == 0:
        return 0 
    elif i == 1:
        return 1
    else:
        dp = [0,1]
        for i in range(n+1):
            if i == 1 or i == 0:
                continue
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]

print(fun(4))
