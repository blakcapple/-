from typing import List
from copy import deepcopy
def solveNQueens(n: int) -> List[List[str]]:
    def backtrack(board, row, n):
        # 终止条件：
        if row >= n:
            result.append(deepcopy(board))
            return 
        # 横向遍历
        for i in range(0, n):
            # 选择动作
            if not isVaild(board, row, i):
                continue
            else:
                board[row][i] = 'Q'
            #纵向递归
            backtrack(board, row+1, n)
            # 撤销动作
            board[row][i] = '.'
            
    def isVaild(board,row, col):
        #判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        # 判断左上角是否冲突
        i = row -1
        j = col -1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i>=0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    backtrack(board, 0, n)
    return result

print(solveNQueens(4))

# def solveNQueens(n: int) -> List[List[str]]:
#     if not n: return []
#     board = [['.'] * n for _ in range(n)]
#     res = []
#     def isVaild(board,row, col):
#         #判断同一列是否冲突
#         for i in range(len(board)):
#             if board[i][col] == 'Q':
#                 return False
#         # 判断左上角是否冲突
#         i = row -1
#         j = col -1
#         while i>=0 and j>=0:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j -= 1
#         # 判断右上角是否冲突
#         i = row - 1
#         j = col + 1
#         while i>=0 and j < len(board):
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j += 1
#         return True

#     def backtracking(board, row, n):
#         # 如果走到最后一行，说明已经找到一个解
#         if row == n:
#             temp_res = []
#             for temp in board:
#                 temp_str = "".join(temp)
#                 temp_res.append(temp_str)
#             res.append(temp_res)
#         for col in range(n):
#             if not isVaild(board, row, col):
#                 continue
#             board[row][col] = 'Q'
#             backtracking(board, row+1, n)
#             board[row][col] = '.'
#     backtracking(board, 0, n)
#     return res



print(solveNQueens(4))
        
    