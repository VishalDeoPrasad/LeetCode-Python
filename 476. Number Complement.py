class Solution(object):
    def binaryConversion(self, N):
        binary = []
        while N>0:
            a = N%2
            binary.append(a)
            N = N//2
        return binary

    def flipbit(self, binary):
        return [0 if b else 1 for b in binary]

    def findComplement(self, num):
        binary = self.binaryConversion(num)
        inverse = self.flipbit(binary)
        ans = 0
        for i in range(len(inverse)):
            ans += inverse[i]*(2**i)
        return ans

print(Solution().findComplement(5))