class Solution(object):
    def convertToBase7(self, num):
        if num == 0: return "0"
        N=abs(num)
        ans = ""
        while N>0:
            a = N%7
            ans = str(a)+ans
            N = N//7
        return "-"+ans if num < 0 else ans
    
print(Solution().convertToBase7(7))