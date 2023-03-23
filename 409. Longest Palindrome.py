class Solution(object):
    def longestPalindrome(self, s):
        word_dic = {}
        for ch in s:
            if ch not in word_dic:
                word_dic[ch] = 1
            else:
                word_dic[ch] += 1
        odd = 0
        for key, value in word_dic.items():
            odd += word_dic[key]%2
        return len(s)-odd+1 if odd > 0 else len(s)

print(Solution().longestPalindrome("aaabbccddd"))