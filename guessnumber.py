# The guess API is already defined for you.
# def guess(num):
#     -1 if num > pick
#      1 if num < pick
#      0 if num == pick

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid  # Found the picked number
            elif res < 0:
                right = mid - 1  # My guess is too high
            else:
                left = mid + 1   # My guess is too low
