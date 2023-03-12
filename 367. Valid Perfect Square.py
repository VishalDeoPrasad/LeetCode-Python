class Solution:
    #idea 1 - Brute-force
    #TC - O(N), SC - O(1)
    def solve1(self, A):
        for i in range(1, A):
            if i == A/i:
                return A/i, True
        return 0, False
    
    #idea 2 - Brute Force slightly better then previous
    #TC - O(N/2), SC - O(1)
    def solve1(self, A):
        for i in range(1, A//2):
            if i == A/i:
                return i, True
        return 0, False
    
    #idea 3 - Binary Search
    #TC - O(log N), SC - O(1)
    def solve(self, num):
        low = 0
        high = num//2
        while low <= high:
            mid = (low+(high-low))//2
            if mid == num//mid and num % mid == 0:
                return True
            
            if mid < (num//mid):
                low = mid + 1
            else:
                high = mid - 1
        return False
    
print(Solution().solve1(1))
        