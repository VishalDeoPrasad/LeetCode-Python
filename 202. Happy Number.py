class Solution(object):
    def digitSquare(self, n):
        SquareSum = 0
        while n>0:
            a = n%10
            SquareSum += a**2
            n = n//10
        return SquareSum

    def isHappy(self, n):
        seen_num = []
        while n!=1:
            n = self.digitSquare(n)
            if n in seen_num:
                return False
            else:
                seen_num.append(n)
        return True
    
print(Solution().isHappy(19))
        