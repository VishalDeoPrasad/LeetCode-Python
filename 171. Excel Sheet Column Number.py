class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for ch in columnTitle:
            temp = ord(ch) - ord('A') + 1
            col_num = col_num*26 + temp
        return col_num

print(Solution().titleToNumber("ZY"))