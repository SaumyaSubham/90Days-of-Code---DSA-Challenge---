# Minimum Depth of Binary Tree                             Difficulty = Easy


# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if root.left and root.right:
            return min(left, right) + 1
        
        return max(left, right) + 1