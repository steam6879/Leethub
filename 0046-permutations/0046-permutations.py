from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return None
            
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    path.append(nums[i])

                    backtrack(path, used)

                    path.pop()
                    used.remove(i)

        backtrack([], set())
        return ans
