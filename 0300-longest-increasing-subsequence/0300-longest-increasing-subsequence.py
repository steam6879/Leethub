class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # This will store the smallest possible tail of an increasing subsequence
        for num in nums:
            idx = bisect_left(sub, num)  # Find the index to replace or append
            if idx == len(sub):
                sub.append(num)  # Extend the subsequence
            else:
                sub[idx] = num  # Replace to maintain optimal subsequence
        return len(sub)