class Solution(object):
    def containsDuplicate(self, nums):
        '''for n in nums:
            if nums.count(n) > 1:
                return True
        return False'''
        temp = set()
        for n in nums:
            if n in temp:
                return True
            else:
                temp.add(n)
        return False

print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))