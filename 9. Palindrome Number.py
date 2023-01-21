class Solution(object):
    def isPalindrome1(self, x):
        if x < 0:
            return "false"
        rev_x = int(str(x)[::-1])
        return "true" if x == rev_x else "false"

    def isPalindrome2(self, x):
        while x > 0:
            rev_x = int(str(x)[::-1])
            return "true" if x == rev_x else "false"
        return "false"
    
    def isPalindrome3(self, x):
        rev_x = str(x)[::-1]
        print(x, rev_x)
        return "true" if str(x) == rev_x else "false"

    def number_reverse(self, x):
        rev_n = 0
        while x > 0:
            a = x % 10  #give last digit
            rev_n = rev_n * 10 + a
            x = x // 10 #remove last digit
        return rev_n
    
    def isPalindrome(self, x):
        if x < 0:
            return "false"
        rev_x = self.number_reverse(x)
        return "true" if x == rev_x else "false"
        

print(Solution().isPalindrome(1101))

