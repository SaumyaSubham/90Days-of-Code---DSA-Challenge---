# Count of Range Sum                                   Difficulty = Hard

# Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

# Example 1:

# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

# Example 2:

# Input: nums = [0], lower = 0, upper = 0
# Output: 1


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
            
		# inclusive
        def mergesort(l,r):
            if l == r:
                return 0
            mid = (l+r)//2
            cnt = mergesort(l,mid) + mergesort(mid+1,r)
			
            i = j = mid+1
            # O(n)
            for left in cumsum[l:mid+1]:
                while i <= r and cumsum[i] - left < lower:
                    i+=1
                while j <= r and cumsum[j] - left <= upper:
                    j+=1
                cnt += j-i
                
            cumsum[l:r+1] = sorted(cumsum[l:r+1])
            return cnt
			
        return mergesort(0,len(cumsum)-1)
    
    