# Binary Tree Inorder Traversal                         Difficulty = Easy


# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]




class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []        
        def inorder(node) :
            if not node :
                return            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)            
            
        inorder(root)
        return res
