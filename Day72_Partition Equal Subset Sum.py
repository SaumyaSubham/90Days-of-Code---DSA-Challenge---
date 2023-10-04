# Partition Equal Subset Sum                      Difficulty = Medium


# Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

# Example 1:

# Input: N = 4
# arr = {1, 5, 11, 5}
# Output: YES
# Explanation: 
# The two parts are {1, 5, 5} and {11}.

# Example 2:

# Input: N = 3
# arr = {1, 3, 5}
# Output: NO
# Explanation: This array can never be 
# partitioned into two such parts.

class Solution:
    def equalPartition(self, N, arr):
        # Calculate the sum of elements in the array
        total_sum = sum(arr)

        # Check if the total sum is odd, which means it's impossible to divide equally
        if total_sum % 2 != 0:
            return 0

        target = total_sum // 2  # The target sum for each partition
        dp = [[False for _ in range(target + 1)] for _ in range(N + 1)]

        # Base case: If the target is 0, we can always achieve it by not selecting any element.
        for i in range(N + 1):
            dp[i][0] = True

        # Fill the DP table
        for i in range(1, N + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return 1 if dp[N][target] else 0
    