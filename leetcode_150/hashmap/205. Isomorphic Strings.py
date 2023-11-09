# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]



class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False