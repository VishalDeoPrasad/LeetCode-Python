class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1]+1
        else:
            dig_2_str = ""
            for d in digits:
                dig_2_str += str(d)
            str_2_dig = int(dig_2_str) + 1
            dig_2_str = str(str_2_dig)
            str_2_dig = [int(dig_2_str[i]) for i in range(len(dig_2_str)) ]
            return str_2_dig
        return digits

s = Solution()
print(s.plusOne([9,8]))

