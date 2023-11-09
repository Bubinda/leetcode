# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited = s.strip().split(' ')
        return len(splited[-1])

# a solution without using build in functions
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length