# Unique Binary Search Trees                             Difficulty = Medium


# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


# Example 1:


# Input: n = 3
# Output: 5

# Example 2:

# Input: n = 1
# Output: 1

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        # Create 'sol' array of length n+1...
        sol = [0] * (n+1)
        # The value of the first index will be 1.
        sol[0] = 1
        # Run a loop from 1 to n+1...
        for i in range(1, n+1):
            # Within the above loop, run a nested loop from 0 to i...
            for j in range(i):
                # Update the i-th position of the array by adding the multiplication of the respective index...
                sol[i] += sol[j] * sol[i-j-1]
        # Return the value of the nth index of the array to get the solution...
        return sol[n]
    