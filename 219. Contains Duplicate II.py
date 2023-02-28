class Solution(object):
    #time complexity O(n*n)
    def containsNearbyDuplicate1(self, nums, k):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i-j) <= k:
                        return True
        return False
    
    #time complexity o(n*k), best o(n),  worst o(n*n)
    def containsNearbyDuplicate2(self, nums, k):
        for i in range(len(nums)-1):
            for j in range(i+1, i+k+1):
                if j < len(nums):
                    if nums[i] == nums[j]:
                        if abs(i-j) <= k:
                            return True
                else:
                    break
        return False
    
    #time complexity o(n)
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for idx, num in enumerate(nums):
            if num in dic and idx-dic[num] <= k:
                return True
        
            dic[num] = idx
        return False


nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))