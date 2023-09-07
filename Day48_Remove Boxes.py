# Remove Boxes                              Difficulty = Hard

# You are given several boxes with different colors represented by different positive numbers.

# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

# Return the maximum points you can get.

 
# Example 1:

# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)

# Example 2:

# Input: boxes = [1,1,1]
# Output: 9

# Example 3:

# Input: boxes = [1]
# Output: 1


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r: return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:  # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                l += 1
                k += 1
            ans = (k+1) * (k+1) + dp(l+1, r, 0)  # Remove all boxes which has the same with `boxes[l]`
            for m in range(l + 1, r + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            return ans

        return dp(0, len(boxes) - 1, 0)
