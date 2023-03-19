class Solution(object):
    def isSubsequence(self, s, t):
        cnt = 0
        i, j = 0,0
        while i < len(s) and j < len(t):
            if cnt == len(s):
                return True

            if s[i] == t[j]:
                print(s[i],t[j])
                cnt += 1
                i += 1
                j += 1
                print(cnt)
            else:
                j += 1
        if cnt == len(s):
            return True

        return False
s = "axc"
t = "ahbgdc"
s1 = "abc"
t2 = "ahbgdc"
s2 = "cabb"
t2 = ""
print(Solution().isSubsequence(s2,t2))