class Solution:
    def reverseBits(self, n):
        rev_bit = 0
        for i in range(32):
            temp = (n >> i) & 1
            rev_bit = rev_bit | (temp << (31 - i))
        return rev_bit

