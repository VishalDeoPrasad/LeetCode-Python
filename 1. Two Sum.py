class Solution:
    #Solution 1
    def twoSum1(self, nums, target):
        pair = []
        [pair.append([i,j]) for i in range(len(nums)-1) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target]
        return pair[0]
    
    #Solution 2
    def twoSum(self, nums, target):
        #solution 2
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return i,j 

s = Solution()
print(s.twoSum([2,3,5,7], 10))
