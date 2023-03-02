class Solution(object):
    def addition(self, n):
        sum = 0
        while n > 0:
            a = n%10
            sum += a
            n = n//10
        return sum

    def addDigits(self, num):
        if num >= 0 and num <= 9:
            return num
        
        total = self.addition(num)
        while total >= 10:
            total = self.addition(total)
        return total
        
print(Solution().addDigits(38))