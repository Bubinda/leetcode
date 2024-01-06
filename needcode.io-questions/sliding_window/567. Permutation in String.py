# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2: return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # initial values for first set of window
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(n2-n1):               # n2-n1 is the number of slides
            if s1Count == s2Count:
                return True
            
            # reduce leaving char count
            s2Count[ord(s2[i]) - ord('a')] -= 1
            
            # increase introduced char count
            s2Count[ord(s2[i+n1]) - ord('a')] += 1

        return s1Count == s2Count    




class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        # get the length of both inputs
        length_t, length_s = len(t), len(s)

        # if our first text is longer than the second the first (t) cannot be a permutated substring of the second (s)
        if length_t > length_s: return False

        # create two frequency counter for the window of the string t and the current windows we are cheing in s
        # they are both consisting of 26 zeros for each letter in the alphabet
        t_freq,curr_window_freq = [0]*26, [0]*26

        # first we go over the string t to get the t_freq window set and also set the current windo to contain the length of t first chars of s
        for chars_of_t in range(length_t):
            # the freqency is set by getting the ordinality of the current read char and the ordinality of the lower case char a 
            # to determine the position of the character relative to 'a' in the Unicode character set.
            t_freq[ord(t[chars_of_t]) - ord('a')] += 1
            curr_window_freq[ord(s[chars_of_t]) - ord('a')] += 1

        # check if wa have a match in our first window
        if t_freq == curr_window_freq: return True

        # then go over the remaing part of s and check for mathing frequency windows
        for remaining_chars_of_s in range(length_t, length_s):

            # for each step we add the current char to the freqeuncy window and delete the char that is on length of t position previous of our current char
            curr_window_freq[ord(s[remaining_chars_of_s]) - ord('a')] += 1
            curr_window_freq[ord(s[remaining_chars_of_s - length_t]) - ord('a')] -= 1

            # then we check again for a match
            if t_freq == curr_window_freq: return True

        # if we do not get any mathes we will return False so that there are no permutatiosn of t in s
        return False
    


# solution by using the counter module -> faster lookups
from collections import Counter

def checkInclusion(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    if len_s1 > len_s2:
        return False
    
    # Count the occurrences of characters in s1
    counter_s1 = Counter(s1)
    
    # Initialize the counter for the first window in s2
    window = Counter(s2[:len_s1])
    
    # Check if the initial window is a permutation of s1
    if window == counter_s1:
        return True
    
    # Iterate through the rest of the windows in s2
    for i in range(len_s1, len_s2):
        # Update the window by adding the new character and removing the first character
        window[s2[i]] += 1
        window[s2[i - len_s1]] -= 1
        
        # Check if the current window is a permutation of s1
        if window == counter_s1:
            return True
    
    # No permutation found
    return False
