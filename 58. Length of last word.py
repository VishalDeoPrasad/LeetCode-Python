import smtplib


class Solution(object):
    def lengthOfLastWord(self, s):
        str_lst = s.split(" ")
        print(str_lst)
        for i in range(1, len(str_lst)):
            if len(str_lst[-i]):
                return len(str_lst[-i])
        

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))