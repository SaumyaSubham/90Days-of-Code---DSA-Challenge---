# Longest Common Substring                           Difficulty = Medium

# Given two strings. The task is to find the length of the longest common substring.


# Example 1:

# Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
# Output: 4
# Explanation: The longest common substring
# is "CDGH" which has length 4.
# Example 2:

# Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
# Output: 1
# Explanation: The longest common substrings
# are "A", "B", "C" all having length 1.


class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0]*(m+1) for _ in range(n+1)]
        count = 0
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
                else:
                    if S1[i-1]==S2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                        count = max(dp[i][j],count)
        return count
    
    