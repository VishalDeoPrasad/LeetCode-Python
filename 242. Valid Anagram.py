class Solution(object):
    def isAnagram(self, s, t):
        #based on obervation
        if len(set(s)) != len(set(t)):
            return False
        if len(s) != len(t):
            return False
        unique = set(s)
        for ch in unique:
            if s.count(ch) != t.count(ch):
                return False
        return True
    
print(Solution().isAnagram("cat","rat"))