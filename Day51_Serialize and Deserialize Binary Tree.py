# Serialize and Deserialize Binary Tree                        Difficulty = Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []
# Output: []


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output =[]
        def check(root):
            if not root:
                output.append("#")
            if root:
                output.append(str(root.val))
                check(root.left)
                check(root.right)
        check(root)
        return ','.join(output)
            
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(",")
        
        def create():
            if node_list:
                value = node_list.pop(0)
                if(value == "#"):
                    return None
                else:
                    node = TreeNode(int(value))
                    node.left= create()
                    node.right = create()
                return node
        
        home = create()
        return home
    
    