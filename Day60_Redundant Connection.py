# Redundant Connection                                         Difficulty = Medium

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

class Disjoint:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
    
    def findUpar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUpar(self.parent[node])
        return self.parent[node]

    def byRank(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)
        if ulp_u==ulp_v:
            return False
        if self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_u]=ulp_v
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        disjoint=Disjoint(n)
        for x,y in edges:
            if disjoint.byRank(x,y)==False:
                lst=[x,y]
        return lst