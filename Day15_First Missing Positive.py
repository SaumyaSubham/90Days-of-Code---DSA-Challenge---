# First Missing Positive                                                 Difficulty = Hard


# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        i = 1
        while i in unique:
            i += 1
        return i
    