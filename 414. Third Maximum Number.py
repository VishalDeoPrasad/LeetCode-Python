class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort(reverse = True)
        return nums[2] if len(nums) > 2 else nums[0]
    
print(Solution().thirdMax([1,2,3,3]))