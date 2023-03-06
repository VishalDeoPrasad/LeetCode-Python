class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.pf = self.prefix_sum(nums)

    def prefix_sum(self, nums):
        pf = []
        pf.append(nums[0])
        for i in range(1, len(nums)):
            pf.append(pf[i-1]+nums[i])
        print(pf)
        return pf      

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pf[right]
        
        return self.pf[right] - self.pf[left-1]

print(NumArray([-2,0,3,-5,2,-1]).sumRange(2,5))
    
