# Sum of Distancs in Tree                                  Difficulty = Hard

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

# Example 1:


# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.

# Example 2:


# Input: n = 1, edges = []
# Output: [0]

# Example 3:


# Input: n = 2, edges = [[1,0]]
# Output: [1,1]



class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ans = 0
        subtree = {}
        
        def dfs(node, prev, depth):
            total = 1
            nonlocal ans
            ans+=depth
            for child in g[node]:
                if child == prev:
                    continue
                total+=dfs(child, node, depth + 1)
            subtree[node] = total
            return total
        
        dfs(0, None, 0)
        res = [0] * n
        res[0] = ans
        
        def dfs2(node, prev):
            for child in g[node]:
                if child == prev:
                    continue
                res[child] = res[node] - subtree[child] + (n-subtree[child])
                dfs2(child, node)
                
        dfs2(0, None)
        return res
