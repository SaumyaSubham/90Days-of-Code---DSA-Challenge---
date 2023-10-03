# Minimum sum of two numbers formed from digits of an array                   Difficulty = Medium

# Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of given array must be used to form the two numbers.

# Examples: 

# Input: [6, 8, 4, 5, 2, 3]
# Output: 604
# The minimum sum is formed by numbers 
# 358 and 246

# Input: [5, 3, 0, 7, 4]
# Output: 82
# The minimum sum is formed by numbers 
# 35 and 047 


from queue import PriorityQueue
 
# Returns sum of two numbers formed
# from all digits in a[]
def solve(a):
     
    # min Heap
    pq = PriorityQueue()
     
    # To store the 2 numbers
    # formed by array elements to
    # minimize the required sum
    num1 = ""
    num2 = ""
 
    # Adding elements in
    # Priority Queue
    for x in a:
        pq.put(x)
 
    # Checking if the priority
    # queue is non empty
    while not pq.empty():
        num1 += str(pq.get())
        if not pq.empty():
            num2 += str(pq.get())   
 
    # The required sum calculated
    sum = int(num1) + int(num2)
     
    return sum
     