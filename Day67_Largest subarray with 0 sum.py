# Largest subarray with 0 sum                                          Difficulty = Medium

# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.


class Solution:
    def maxLen(self, n, arr):
        #Code here
        maxi=0
        s =0
        d={}
        for i in range(n):
            s+=arr[i]
            if s==0:
                maxi = i+1
            elif s in d:
                maxi = max(maxi,i-d[s])
            else:
                d[s]=i
        return maxi