class Solution(object):
    def hammingDistance(self, x, y):
        n = x^y
        cnt = 0
        while n>0:
            cnt += n&1
            n = n>>1
        return cnt
    
print(Solution().hammingDistance(3,6))