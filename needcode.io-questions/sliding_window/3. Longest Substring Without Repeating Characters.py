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
 



# why so ever this does not work but should
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, high = 0,0
        sub = []
        max_length = 0

        while low and high < len(s):
            print('go')
            if s[high] not in sub:
                sub.append(s[high])
                high += 1
                max_length = max(len(sub), max_length)
                print(high, s[high], sub)
            else:
                low += 1
                high = low
                sub = []

        return max_length


# this works
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last seen index of each character.
        char_index = {}
        max_length = 0
        start = 0

        for i in range(len(s)):
            # If the character is already in the dictionary and its last seen index is greater than or equal to the start,
            # update the start to the next position of the repeating character.
            if s[i] in char_index and char_index[s[i]] >= start:
                start = char_index[s[i]] + 1
            char_index[s[i]] = i  # Update the last seen index of the character.
            max_length = max(max_length, i - start + 1)

        return max_length
