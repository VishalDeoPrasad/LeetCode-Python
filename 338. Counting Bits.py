class Solution:
    def setBit(self, n):
        cnt = 0
        while n>0:
            cnt += n%2
            n = n//2
        return cnt
    def countBits(self, n):
        set_bit = [self.setBit(i) for i in range(n+1)]

        return set_bit

print(Solution().countBits(6))
        