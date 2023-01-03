class Solution:
    #method 2
    def twoSum(self, nums, target):
        pair = []
        [pair.append([i,j]) for i in range(len(nums)-1) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target]
        return pair[0]

s = Solution()
print(s.twoSum([2,3,5,7], 10))
