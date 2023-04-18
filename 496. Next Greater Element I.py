class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        aux_dic = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i] < nums2[j]:
                    aux_dic[nums2[i]] = nums2[j]
                    break
                if j == len(nums2)-1:
                    aux_dic[nums2[i]] = -1

        aux_dic[nums2[i]] = -1
        ans = [aux_dic[key] for key in nums1]
        return ans
    
nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(Solution().nextGreaterElement(nums1, nums2))