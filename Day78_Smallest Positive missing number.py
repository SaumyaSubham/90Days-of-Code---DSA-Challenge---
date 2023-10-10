# Smallest Positive missing number                   Difficulty = Medium

# You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

# Note: Positive number starts from 1.

# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing 
# number is 6.
# Example 2:

# Input:
# N = 5
# arr[] = {0,-10,1,3,-20}
# Output: 2
# Explanation: Smallest positive missing 
# number is 2.


class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        for i in range(len(arr)):
            if arr[i]<0:
                arr[i]=0
        for i in range(len(arr)):
            element=abs(arr[i])
            if element-1<0 or element-1>=len(arr):
                continue
            if arr[element-1]<0:#already visited
                continue
            if arr[element-1]>0:
                arr[element-1]=-1*arr[element-1]
                continue
            arr[element-1]=-(len(arr)+2)
        for i in range(len(arr)+1):
            if i==len(arr):
                return i+1
            if arr[i]>=0:
                return i+1
            
            