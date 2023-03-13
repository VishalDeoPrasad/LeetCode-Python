class Solution:
    #idea 1 - Brute-force
    #TC - O(N), SC - O(1)
    def solve(self, A):
        if A == 1: return True
        for i in range(1, A):
            if i == A/i:
                return True
        return False
    
    #idea 2 - Brute Force slightly better then previous
    #TC - O(N/2), SC - O(1)
    def solve1(self, A):
        if A == 1: return True
        for i in range(1, A//2):
            if i == A/i:
                return i, True
        return False
    
    #idea 3 - Binary Search
    #TC - O(log N), SC - O(1)
    def isPerfectSquare(self, num):
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            #if mid * mid == num:
            if mid == num/mid:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
print(Solution().solve1(1))
print(Solution().isPerfectSquare(1))
        