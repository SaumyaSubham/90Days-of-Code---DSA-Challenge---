# Pallindrome Pairs                              Difficulty = Hard

# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a 
# palindrome
# .
# Return an array of all the palindrome pairs of words.

 
# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
      ans = []   # initialize a list to store the palindrome pairs
      dict = {word[::-1]: i for i, word in enumerate(words)}  # create a dictionary to store the reverse of words and their indices

      for i, word in enumerate(words):  # iterate through the words and their indices
         if "" in dict and dict[""] != i and word == word[::-1]:  # check if empty string is in the dictionary and the current word is palindrome
               ans.append([i, dict[""]])  # append the indices to the ans list

         for j in range(1, len(word) + 1):  # iterate through the word characters
                l = word[:j]  # get the left substring
                r = word[j:]  # get the right substring
                if l in dict and dict[l] != i and r == r[::-1]:  # check if left substring is in the dictionary and the right substring is palindrome
                   ans.append([i, dict[l]])  # append the indices to the ans list
                if r in dict and dict[r] != i and l == l[::-1]:  # check if right substring is in the dictionary and the left substring is palindrome
                   ans.append([dict[r], i])  # append the indices to the ans list

      return ans  # return the ans list