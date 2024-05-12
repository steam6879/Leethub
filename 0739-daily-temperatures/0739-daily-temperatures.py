from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = []

        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                index = stack.pop()
                ret[index] = i - index

            stack.append(i)
            
        return ret