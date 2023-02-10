class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        sheet_number = ""
        while columnNumber:
            last = chr((columnNumber-1) % 26 + ord("A"))
            sheet_number = last + sheet_number
            columnNumber = (columnNumber-1)//26
        return sheet_number

print(Solution().convertToTitle(701))