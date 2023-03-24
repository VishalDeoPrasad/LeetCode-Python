class Solution(object):
    def countSegments(self, s):
        return len(s.strip().split())
    
s = "Hello, my name is John"
print(Solution().countSegments(s))