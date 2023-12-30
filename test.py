class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = self.nums
        target = self.target
        
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] == target:
                return [nums[i], nums[i + 1]]
            
        return -1
            
if '__name__' == '__name__':
    
    
    print(Solution.twoSum([1, 2, 3 ,4, 5], 7))