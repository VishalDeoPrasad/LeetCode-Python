class Solution(object):
    #idea 1 - Linear Approch
    #TC - O(N) SC - O(1)
    def arrangeCoins1(self, n):
        a = n
        cnt = 0
        for i in range(1, n+1):
            a = a-i
            if a >= 0:
                cnt += 1
            else:
                return cnt
        return cnt
    
    #idea 2 - binary Search (N*(N+1))/2
    #TC - O(log N) SC - O(1)
    def arrangeCoins2(self, n):
        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            if (mid*(mid+1))/2 == n:
                return mid
            elif (mid*(mid+1))/2 > n:
                right = mid - 1
            elif (mid*(mid+1))/2 < n:
                left = mid + 1
        return left-1
    
   
print(Solution().arrangeCoins(10))