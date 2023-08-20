# Minimum Cost to Merge Stones                         Difficulty = Hard


# There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

# A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

# Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

 

# Example 1:

# Input: stones = [3,2,4,1], k = 2
# Output: 20
# Explanation: We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
# Example 2:

# Input: stones = [3,2,4,1], k = 3
# Output: -1
# Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.



class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones)-1) % (k-1): return -1 # impossible
        
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
        
        @cache
        def fn(lo, hi): 
            """Return min cost of merging stones[lo:hi]."""
            if hi - lo < k: return 0 # not enough stones
            ans = inf 
            for mid in range(lo+1, hi, k-1): 
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            if (hi-lo-1) % (k-1) == 0: ans += prefix[hi] - prefix[lo]
            return ans 
        
        return fn(0, len(stones))
