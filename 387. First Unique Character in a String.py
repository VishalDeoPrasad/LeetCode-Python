class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == len(set(s))/2:
            return -1
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
    
print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))