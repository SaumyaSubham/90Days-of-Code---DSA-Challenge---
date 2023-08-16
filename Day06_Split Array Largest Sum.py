# Split Array Largest Sum                         Difficulty = Hard


# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.



class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo+hi)//2
            tot, cnt = 0, 1
            for num in nums:
                if tot+num<=mid: 
                    tot += num
                else:
                    tot = num
                    cnt += 1
            
            if cnt>k: lo = mid+1
            else: hi = mid
        return hi
