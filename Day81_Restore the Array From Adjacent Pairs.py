# Restore the Array From Adjacent Pairs                           Difficulty = Medium

# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

# Return the original array nums. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        
        for u, v in adjacentPairs:
            g[u].append(v)
            g[v].append(u) 

        N = len(g)
        result = [0]*N
        added_first = False
        
        for k, v in g.items():
            if len(v) == 1:
                if added_first:
                    result[N-1] = k
                else:
                    result[0] = k
                    added_first = True
        
        l, r = 1, N-2
        le, re = result[0], result[N-1]
                    
        while l<=r:
            result[l] = g[le][0] if len(g[le]) == 1 or g[le][1] == result[l-2] else g[le][1]
            result[r] = g[re][0] if len(g[re]) == 1 or g[re][1] == result[r+2] else g[re][1]
            le, re = result[l], result[r]
            l+=1
            r-=1
        
        return result
    
    