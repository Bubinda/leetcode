# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            sett.add(s[r])
            max_len = max(max_len, r-l+1)

        return max_len
    


# solution by using a dict to take trak of the last index of the characters we have already visisted
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_dict = {}
        left = 0
        max_substring = 0

        for right in range(len(s)):
            # if our current char is not in the visited chars we can increase the max substring 
            if s[right] not in visited_dict:
                max_substring = max(max_substring, (right-left+1)) 
            # if it is in the visited chars we have to differentiate between two cases:
            # 1. the char index is outside of the current window between left and right index, then we can increase our max_sequence without any problems
            # 2. the char index is inside our current window then we need to set our left pointer index to the next larger postiion of the last index where the current char appeared so we exclude this char from our current window
            else:
                if visited_dict[s[right]] < left:
                    max_substring = max(max_substring, (right-left+1))
                else:
                    left = visited_dict[s[right]] + 1
            # in the end we alsways add the current index to the visisted dictionary of all the chars we have seen so far
            visited_dict[s[right]] = right

        return max_substring
