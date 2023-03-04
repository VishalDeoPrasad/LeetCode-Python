class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #make a dictionary if elements already exist check old value and new value
        #else append new element
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
            
        word_dict = {}
        for key, val in zip(pattern, s):
            if key not in word_dict:
                if val not in word_dict.values():
                    word_dict[key] = val
                else:
                    return False
            else:
                if word_dict[key] != val:
                    return False
        
        return True
p = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(p,s))