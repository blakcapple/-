# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
from typing import List
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         def backtrack(intervals):            
#             result = []
#             pass_list_index = []
#             for i, list in enumerate(intervals):
#                 for j in range(i+1, len(intervals)):
#                     if i in pass_list_index or j in pass_list_index:
#                         continue
#                     start = list[0]
#                     end = list[1]
#                     if start <= intervals[j][0] and end >= intervals[j][0]:
#                         if end > intervals[j][1]:
#                             new_list = [start, end]
#                         elif end <= intervals[j][1]:
#                             new_list = [start, intervals[j][1]]
#                         result.append(new_list)
#                         pass_list_index.append(i)
#                         pass_list_index.append(j)
#                         break
#                     if intervals[j][1] >= start and end >= intervals[j][1]:
#                         if start >= intervals[j][0]:
#                             new_list = [intervals[j][0], end]
#                         elif start < intervals[j][0]:
#                             new_list = [start, end]
#                         result.append(new_list)
#                         pass_list_index.append(i)
#                         pass_list_index.append(j)
#                         break
#                     if intervals[j][1]>= end and intervals[j][0] <= start:
#                         new_list = intervals[j][:]
#                         result.append(new_list)
#                         pass_list_index.append(i)
#                         pass_list_index.append(j)
#                         break
#             for i, list in enumerate(intervals):
#                 if i in pass_list_index:
#                     continue
#                 result.append(list)
#             if len(pass_list_index) == 0:
#                 return result
#             result = backtrack(result)
#             return result
#         result = backtrack(intervals)
#         return result
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
s = Solution()
intervals = [[1,4],[0,2],[3,5]]
print(s.merge(intervals))
            
        