class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i

print(Solution().missingNumber([0,1,3]))
