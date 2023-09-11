# Valid Palindrome II                                Difficulty = Easy

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

class Solution:
    def validPalindrome(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True
        
