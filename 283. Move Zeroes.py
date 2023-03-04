class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        left = 0
        right = 0
        while right < n:
            if nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right += 1
        return nums
    
print(Solution().moveZeroes([0,1,0,3,12]))