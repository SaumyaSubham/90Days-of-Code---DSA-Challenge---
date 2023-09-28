# Valid Pair Sum                               Difficulty = Medium


# Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.

# Example 1:

# Input: N = 3, a[] = {3, -2, 1}
# Output: 2
# Explanation: {3, -2}, {3, 1} are two 
# possible pairs.

# Example 2:

# Input: N = 4, a[] = {-1, -1, -1, 0}
# Output: 0
# Explanation: There are no possible pairs.

class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
    	a.sort(reverse = True) # sort array
        low, high = 0, n-1
        count = 0
        
        while low <= high:
            msum = a[low] + a[high]
        
            if msum <= 0:
                high -= 1
        
            else:
                count += high -low
                low += 1
        return count