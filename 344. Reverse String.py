class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2):
            j = len(s)-1-i
            s[i], s[j]= s[j], s[i]
        return s

print(Solution().reverseString(['H','e','l','l','o']))