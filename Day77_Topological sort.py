# Topological sort                                        Difficulty = Medium

# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

# Example 1:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 3, 2, 1, 0.
# Example 2:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 5, 4, 2, 1, 3, 0.

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        vis=[0]*V
        stack=[]
        def dfs(i):
            vis[i]=1
            for it in adj[i]:
                if not vis[it]:
                    dfs(it)
            stack.append(i)
        for i in range(V):
            if not vis[i]:
                dfs(i)
        
        
        return stack[::-1]
    