# Count BST nodes that lie in a given range                       Difficulty = Medium

# Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.

# The values smaller than root go to the left side
# The values greater and equal to the root go to the right side

# Example 1:

# Input:
#       10
#      /  \
#     5    50
#    /    /  \
#   1    40  100
# l = 5, h = 45
# Output: 3
# Explanation: 5 10 40 are the node in the
# range

# Example 2:

# Input:
#      5
#     /  \
#    4    6
#   /      \
#  3        7
# l = 2, h = 8
# Output: 5
# Explanation: All the nodes are in the
# given range.

class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        if root == None:
            return 0
        if root.data >= low and root.data<= high:
            return 1+self.getCount(root.left,low,high)+self.getCount(root.right,low,high)
        elif root.data<low:
            return self.getCount(root.right,low,high)
        else:
            return self.getCount(root.left,low,high)
        