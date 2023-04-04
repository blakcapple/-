# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，
# 并返回该子网格中的元素数量。如果不存在，则返回 0。

from typing import List
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        up = [[0 for _ in range(n+1)] for _ in range(m+1)] # 以索引为起点上方连续的1的数量
        left = [[0 for _ in range(n+1)] for _ in range(m+1)] # 以索引为起点左方连续的1的数量
        max_side = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 1: 
                    up[i][j] = up[i-1][j]+1
                    left[i][j] = left[i][j-1]+1
                    board = min(up[i][j], left[i][j])
                    while left[i-board+1][j] < board or up[i][j-board+1] < board: # 通过left 和 up来推断right和down
                        board -= 1

                    max_side = max(max_side, board)
        return max_side*max_side

grid = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
print(s.largest1BorderedSquare(grid))