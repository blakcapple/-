#给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

#请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 本题有bug，如果m和n的取值超过了字符串中最多的0和1的数量，则下面这种解法就不正确，但在力扣上是能通过下面这种解法的
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            # 计算 0 和 1 的数量
            zero_num = 0
            one_num = 0
            for s in str:
                if s == '0':
                    zero_num += 1
                elif s == '1':
                    one_num += 1
            for i in range(m, zero_num-1, -1):
                for j in range(n, one_num-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num]+1)
        print(dp)
        return dp[-1][-1]
    
s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 2
n = 2

print(s.findMaxForm(strs, m,n))


def fun(input, m, n):
    
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for item in input:
        count_of_0 = 0
        count_of_1 = 0
        for s in item:
            if s == '0':
                count_of_0 += 1
            if s == '1':
                count_of_1 += 1
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                dp[i][j] = dp[i][j] + 1    
    
    
    