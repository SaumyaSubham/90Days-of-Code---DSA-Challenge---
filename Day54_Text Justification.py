# Text Justification                                 Difficulty = Hard



# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, cur = [], []
        chars = 0
        
        for word in words:
            # if cur is empty or the total chars + total needed spaces + next word fit
            if not cur or (len(word) + chars + len(cur)) <= maxWidth:
                cur.append(word)
                chars += len(word)
            else:
                # place spaces, append the line to the ans, and move on
                line = self.placeSpacesBetween(cur, maxWidth - chars)
                ans.append(line)
                cur.clear()
                cur.append(word)
                chars = len(word)
        
        # left justify any remaining text, which is easy
        if cur:
            extra_spaces = maxWidth - chars - len(cur) + 1
            ans.append(' '.join(cur) + ' ' * extra_spaces)
            
        return ans
    
    
    def placeSpacesBetween(self, words, spaces):
        if len(words) == 1: return words[0] + ' ' * spaces
        
        space_groups = len(words)-1
        spaces_between_words = spaces // space_groups
        extra_spaces = spaces % space_groups
        
        cur = []
        for word in words:
            cur.append(word)
            
            # place the min of remaining spaces or spaces between words plus an extra if available
            cur_extra = min(1, extra_spaces)
            spaces_to_place = min(spaces_between_words + cur_extra, spaces)

            cur.append(' ' * spaces_to_place)
            
            if extra_spaces: extra_spaces -= 1
            spaces -= spaces_to_place
        
        return ''.join(cur)
