# Strongly Connected Components (Kosaraju's Algo)              Difficulty = Medium
                               
# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

# Example 1:

# Input:

# Output:
# 3
# Explanation:

# We can clearly see that there are 3 Strongly
# Connected Components in the Graph
# Example 2:

# Input:

# Output:
# 1
# Explanation:
# All of the nodes are connected to each other.
# So, there's only one SCC.

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(v)

        def reverse_graph():
            reversed_adj = [[] for _ in range(V)]
            for v in range(V):
                for neighbor in adj[v]:
                    reversed_adj[neighbor].append(v)
            return reversed_adj

        def dfs_reverse(v, visited):
            visited[v] = True
            for neighbor in reversed_adj[v]:
                if not visited[neighbor]:
                    dfs_reverse(neighbor, visited)

        # Step 1: First DFS to fill the stack
        stack = []
        visited = [False] * V
        for v in range(V):
            if not visited[v]:
                dfs(v, visited, stack)

        # Step 2: Reverse the graph
        reversed_adj = reverse_graph()

        # Step 3: Second DFS on the reversed graph to count SCCs
        visited = [False] * V
        scc_count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                dfs_reverse(v, visited)
                scc_count += 1

        return scc_count
    