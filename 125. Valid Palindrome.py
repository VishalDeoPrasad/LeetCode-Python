class Solution:
    def removeSpeical(self, s):
        s = "".join(ch for ch in s if ch.isalnum())
        return s

    def reverseString(self, s):
        #return s[::-1].lower()
        #rev_s = "".join(s[-i] for i in range(1, len(s)+1))
        rev_s = ""
        for ch in s:
            rev_s = ch + rev_s
        return rev_s

    def isPalindrome1(self, s: str) -> bool:
        s = s.lower()
        s = self.removeSpeical(s)
        print(s)
        rev_s = self.reverseString(s)
        print(rev_s)
        return s == rev_s
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = self.removeSpeical(s)
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))