class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x # sqrt(0)=0, sqrt(1)=1

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid # perfect square found
            elif square < x:
                ans = mid   # store last valid mid
                left = mid + 1 # move right
            else:
                right = mid - 1 # move right

        return ans # floor of sqrt(x)



