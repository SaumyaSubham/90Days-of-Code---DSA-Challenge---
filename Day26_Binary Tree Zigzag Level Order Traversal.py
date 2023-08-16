# Binary Tree Zigzag Level Order Traversal                    Difficulty = Medium

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root] if root else [])
        while q :
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            level = reversed(level) if len(res) % 2 else level
            res.append(level)
        return res