class Solution:
    def findTheDifference1(self, s, t):
        for ch in t:
            if ch not in s:
                return ch
            if t.count(ch) > s.count(ch):
                return ch
    
    def findTheDifference2(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
    
    def findTheDifference3(self, s, t):
        s_dic = {}
        for ch in s:
            if ch not in s_dic:
                s_dic[ch] = 1
            else:
                s_dic[ch] = s_dic[ch] + 1
        
        for ch in t:
            if ch not in s_dic:
                return ch
            else:
                if t.count(ch) != s_dic[ch]:
                    return ch
                
    def findTheDifference(self, s, t):
        s_sum = 0
        t_sum = 0
        for ch in s:
            s_sum += ord(ch)
        for ch in t:
            t_sum += ord(ch)
        
        return chr(t_sum-s_sum)
            
    
            
print(Solution().findTheDifference("aab", "aabb"))