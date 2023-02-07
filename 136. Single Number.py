class Solution:
    def singleNumber1(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
    def singleNumber(self, nums):
        unique = 0
        for num in nums:
            unique = unique ^ num
        return unique

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))