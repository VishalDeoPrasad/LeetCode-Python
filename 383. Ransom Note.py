class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) == 0:
            return True
        
        u = set(ransomNote)
        for ch in u:
            if ransomNote.count(ch) > magazine.count(ch):
                return False

        return True 

print(Solution().canConstruct("aa", "aab"))