class Solution:
    def valueof(self, symbol):
        symbol_dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return symbol_dict[symbol]
    
    def romanToInt1(self, s):  # "LVIII"
        result = self.valueof(s[-1])
        n = len(s)
        [result := result+self.valueof(s[i]) for i in range(-2, -n-1, -1) if self.valueof(s[i]) >= self.valueof(s[i+1]) else result := result-self.valueof(s[i])]
            
                
            
        return result
    
    def romanToInt1(self, s):  # "LVIII"
        result = self.valueof(s[-1])
        n = len(s)
        for i in range(-2, -n-1, -1):
            if self.valueof(s[i]) >= self.valueof(s[i+1]):
                result += self.valueof(s[i])
            else:
                result -= self.valueof(s[i])
        return result

s = Solution()
test1 = "LVIII"
test2 = "MCMXCIV"
print(s.romanToInt(test2))
