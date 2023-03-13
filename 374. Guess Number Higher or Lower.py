class Solution(object):
    def guessNumber(self, n):
        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid-1
            else:
                left = mid+1
