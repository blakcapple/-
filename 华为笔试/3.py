input = [1,5,3,4,6,5,1]
import numpy as np
class Solution():
    def function(self, input):
        left_depth = input[0]
        right_dept = input[-1]
        direction = [] # 0 表示向左，1表示向右, 3表示引流点
        water_point = []
        for i in range(1, len(input)-1):
            if input[i] > input[i-1] and input[i] > input[i+1]:
                water_point.append(i)
                direction.append(3)
            elif input[i] == input[i-1] and input[i] > input[i+1]:
                direction.append(3)
                water_point.append(i)
            elif input[i] == input[i+1] and input[i] > input[i-1]:
                direction.append(3)
                water_point.append(i)
            elif input[i] < input[i-1] and input[i] < input[i+1]:
                if input[i-1] > input[i+1]:
                    direction.append(0)
                elif input[i-1] < input[i+1]:
                    direction.append(1)
                else:
                    direction.append(0)
            elif input[i] < input[i-1]:
                direction.append(0)
            elif input[i] < input[i+1]:
                direction.append(1)
            else:
                direction.append(4)
        reslut = [0 for i in range(len(water_point))]
        for value in direction:
            if value == 0:
                r
            
        return direction

s = Solution()
print(s.function(input))

            
            