# Mobile numeric keypad                                   Difficulty = Medium


# Given the mobile numeric keypad. You can only press buttons that are up, left, right, or down to the current button or the current button itself (like 00,11, etc.). You are not allowed to press the bottom row corner buttons (i.e. * and # ). Given a number N, the task is to find out the number of possible numbers of the given length.

# Example 1:

# Input: 1
# Output: 10
# Explanation: Number of possible numbers 
# would be 10 (0, 1, 2, 3, ., 9)  

# Example 2:
# Input: N = 2
# Output: 36
# Explanation: Possible numbers: 00, 08, 11,
# 12, 14, 22, 21, 23, 25 and so on.
# If we start with 0, valid numbers 
# will be 00, 08 (count: 2)
# If we start with 1, valid numbers 
# will be 11, 12, 14 (count: 3)
# If we start with 2, valid numbers 
# will be 22, 21, 23,25 (count: 4)
# If we start with 3, valid numbers 
# will be 33, 32, 36 (count: 3)
# If we start with 4, valid numbers 
# will be 44,41,45,47 (count: 4)
# If we start with 5, valid numbers 
# will be 55,54,52,56,58 (count: 5) 
# and so on..

class Solution:
	def getCount(self, N):
		# code here
		def dfs(i,j , k):
		    
		    if i<0 or j < 0 or i > 3 or j > 2 or (i == 3 and j == 0) or (i==3 and j == 2): return 0
   
		    if k == N:
		        return 1 
		        
	        ## put your dp condition under all base condition , not in between otherwise will get ambigious answer      
	        if dp[i][j][k] != -1: 
		        return dp[i][j][k]
		    
		    if k < N:
		        #take
		        cnt1 = dfs(i,j,k+1)
		        cnt2 = dfs(i-1,j,k+1)
		        cnt3 = dfs(i,j-1,k+1)
		        cnt4 = dfs(i+1,j,k+1)
		        cnt5 = dfs(i,j+1,k+1)
		    
		    dp[i][j][k] = cnt1 + cnt2 + cnt3 + cnt4 + cnt5 
		    return cnt1 + cnt2 + cnt3 + cnt4 + cnt5 
		    
		count = 0 
		
		for i in range(4):
		    for j in range(3):
		        dp = [[[-1]*N for j in range(3)] for i in range(4)]
		        cnt = dfs(i,j,1)
		        count += cnt


        return count