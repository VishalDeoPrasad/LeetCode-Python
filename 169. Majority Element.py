class Solution:
    def majorityElement(self, nums):
        unique_num = set(nums)
        major_elm = 0
        major_elem_freq = 0
        for n in unique_num:
            curr_freq = nums.count(n)
            if major_elem_freq < curr_freq:
                major_elem_freq = curr_freq
                major_elm = n
        return major_elm
nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))