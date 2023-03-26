class Solution(object):
    def findContentChildren(self, g, s):
        i = 0 #cookies
        j = 0 #greed
        s.sort()
        g.sort()
        while i < len(s) and j < len(g):
            #print((i,j), end=" ")
            if s[i] >= g[j]:
                print(s[i], g[j])
                j += 1
            i += 1
        return j
    
g = [5,6,4,2,3]
s = [5,1,2,2,3]

print(Solution().findContentChildren(g,s))