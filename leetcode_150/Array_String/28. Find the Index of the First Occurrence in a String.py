# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start, end = 0,len(needle)

        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            end += 1
            start += 1
            
        return -1
                

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len (haystack)
        m = len (needle)

        for i in range (n):
            j = 0
            for k in range(i, n):
                if haystack[k] == needle[j]: j += 1
                else:
                    break
                if j == m:
                    return i
        return -1