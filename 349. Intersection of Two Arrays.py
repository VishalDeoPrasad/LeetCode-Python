#Idea search each unique element in both array if exist store and return 
# TC - O(N*N) SC - O(N)
class Solution(object):
    def intersection1(self, nums1, nums2):
        unique = set(nums1)
        result = []
        for el in unique:
            if el in nums1 and el in nums2:
                result.append(el)
        return result
    
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))