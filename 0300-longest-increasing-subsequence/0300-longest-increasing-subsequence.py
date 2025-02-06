class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums: return 0

        sub = []
        for num in nums:
            if not sub or num > sub[-1]:
                sub.append(num)

            else:
                left, right = 0, len(sub) - 1
                while left <= right:
                    mid = (left + right) // 2

                    if sub[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                sub[left] = num
        
        return len(sub)
