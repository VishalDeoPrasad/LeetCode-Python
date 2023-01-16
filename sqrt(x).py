def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        L, R = 1, x
        while L <= R:
            mid = L + (R-L)//2
            if mid*mid > x:
                R = mid-1
            elif mid*mid < x:
                L = mid + 1
            else:
                return mid
        return R

print(mySqrt(9))
