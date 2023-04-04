class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.upper()
        cnt = 0
        license = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                if cnt == k:
                    license = "-"+license
                    cnt = 0
                license = s[i]+license
                cnt += 1
        return license
print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(Solution().licenseKeyFormatting(s = "2-5g-3-J", k = 2))
print(Solution().licenseKeyFormatting("--a-a-a-a--", 2))