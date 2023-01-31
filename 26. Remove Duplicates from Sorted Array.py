class Solution(object):
    def removeDuplicates(self, nums):
        i, j = 1, 1
        while j < len(nums):     
            if nums[j-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))