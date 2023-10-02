# Weighted Job Scheduling                               Difficulty = Medium

# Given N jobs where every job is represented by following three elements of it.

# Start Time
# Finish Time
# Profit or Value Associated (>= 0)
# Find the maximum profit subset of jobs such that no two jobs in the subset overlap. 

# Example: 

# Input: Number of Jobs n = 4
#        Job Details {Start Time, Finish Time, Profit}
#        Job 1:  {1, 2, 50} 
#        Job 2:  {3, 5, 20}
#        Job 3:  {6, 19, 100}
#        Job 4:  {2, 100, 200}
# Output: The maximum profit is 250.
# We can get the maximum profit by scheduling jobs 1 and 4.
# Note that there is longer schedules possible Jobs 1, 2 and 3 
# but the profit with this schedule is 20+50+100 which is less than 250.


from functools import cmp_to_key
 
# A job has start time, finish time and profit
class Job:
     
    def __init__(self, start, finish, profit):
         
        self.start = start
        self.finish = finish
        self.profit = profit
 
# A utility function that is used for
# sorting events according to finish time
def jobComparator(s1, s2):
     
    return s1.finish < s2.finish
 
# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1
def latestNonConflict(arr, i):
     
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
             
    return -1
 
# A recursive function that returns the
# maximum possible profit from given
# array of jobs. The array of jobs must
# be sorted according to finish time
def findMaxProfitRec(arr, n):
     
    # Base case
    if n == 1:
        return arr[n - 1].profit
 
    # Find profit when current job is included
    inclProf = arr[n - 1].profit
    i = latestNonConflict(arr, n)
     
    if i != -1:
        inclProf += findMaxProfitRec(arr, i + 1)
 
    # Find profit when current job is excluded
    exclProf = findMaxProfitRec(arr, n - 1)
    return max(inclProf, exclProf)
 
# The main function that returns the maximum
# possible profit from given array of jobs
def findMaxProfit(arr, n):
     
    # Sort jobs according to finish time
    arr = sorted(arr, key = cmp_to_key(jobComparator))
    return findMaxProfitRec(arr, n)

 
print("The optimal profit is", findMaxProfit(arr, n))