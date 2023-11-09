# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        return s_dict == t_dict


#simplest python solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
