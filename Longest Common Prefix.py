class Solution(object):

    def findSubstring(self, str):
        return [str[i][:j] for i in range(len(str)) for j in range(1, len(str[i])+1)]
            
            
    def longestCommonPrefix(self, strs):
        substring = self.findSubstring(strs)
        unique_substring = set(substring)
        print(substring)
        substring_dict = {}
        for sub in unique_substring:
            substring_dict[sub] = substring.count(sub)  
        print(substring_dict)     
        print(max(substring_dict)) 

        
s = Solution()
#substring = s.findSubstring(["flower","flow","flight"])

s.longestCommonPrefix(["flower","flow","flight"])