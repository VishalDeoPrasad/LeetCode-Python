class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_list = [i for i in range(1, len(nums)+1)]
        nums = list(set(nums))
        for i in range(len(nums)):
            num_list.remove(nums[i])
        return num_list
    
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))