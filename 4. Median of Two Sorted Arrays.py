class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n%2 == 1:
            return nums1[n//2]
        else:
            mid = n//2
            return (nums1[mid]+nums1[mid-1])/2
        
ans = Solution().findMedianSortedArrays([1,2],[3,4])
print(ans)