class Solution(object):
    def search(sels, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # Find the middle index

            if nums[mid] == target:
                return mid              # Target found
            elif nums[mid] < target:
                left = mid + 1          # Search in the right half
         else:
            right = mid - 1

       return -1


