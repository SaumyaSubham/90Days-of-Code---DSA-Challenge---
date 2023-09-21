# Most Stones Removed with Same Row or Column                   Difficulty = Medium

# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        
        for a,b in stones:
            row_dict[a].append(b)
            col_dict[b].append(a)
        
        visited = set()

        ans = 0
        que = deque()
        for a,b in stones:
            if (a,b) not in visited:
                #BFS start here for each connected component
                que.append((a,b))
                
                while que:
                    x,y = que.popleft()
                    if (x,y) in visited:
                        continue
                        
                    visited.add((x,y))
                    ans+=1
                    for e in row_dict[x]:  #append all points which are in same line as (x,y)
                        if e!=y:
                            que.append((x,e))
                                            
                    for e in col_dict[y]:  #append all points which are in same column as (x,y)
                        if e!=x:
                            que.append((e,y))
                            
                            
                    # here are two line which make code time complexity O(n^2) to O(n) :-
                    # if any point covers its entire row and column points, then again no need to cover these points again.
                    
                    row_dict[x].clear()
                    col_dict[y].clear()
                
                # each component can not destroy it self completely , there is only one point always exist , so
                ans -=1    
            
        return ans