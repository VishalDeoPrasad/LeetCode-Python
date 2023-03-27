class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        rep = ""
        for i in range(n//2):
            rep +=s[i]
            if n%len(rep) == 0:
                if rep*(n//len(rep)) == s:
                    return True
        return False
        
print(Solution().repeatedSubstringPattern("abcabc"))