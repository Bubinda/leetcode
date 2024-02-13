# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left,right = 0,0
        while right < len(t) and left < len(s):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)
    


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s = len(s)
        t = len(t)

        if s == '': return True
        if s > t: return False 

        j = 0
        for i in range(t):
            if s[j] == t[i]:
                j += 1
            if j == s:
                return True
        return False






















































































