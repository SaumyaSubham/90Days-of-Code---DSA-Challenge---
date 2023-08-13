# Kth Smallest Element in a BST                      Difficulty = Medium


# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = [(root, False)]
        while stack and len(res) < k:
            node, visited = stack.pop()
            if not node:
                continue

            if visited:
                res.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

        return res[-1]
    
    