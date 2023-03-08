class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        n = len(s)
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        i = 0
        j = n - 1
        while i < j:
            while s[i] not in vowel:
                if i >= j:
                    return "".join(s)
                i += 1
            while s[j] not in vowel:
                if i >= j:
                    return "".join(s)
                j -= 1
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
    
print(Solution().reverseVowels("Leetcode"))