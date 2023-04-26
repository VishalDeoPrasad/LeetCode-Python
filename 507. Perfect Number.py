class Solution(object):
    def factors(self, num):
        fact = []
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                fact.append(i)
                fact.append(num//i)
        fact.remove(num)
        return fact

    def checkPerfectNumber(self, num):
        if num == 1: return False
        if sum(self.factors(num)) == num:
            return True
        return False
    
print(Solution().checkPerfectNumber(28))