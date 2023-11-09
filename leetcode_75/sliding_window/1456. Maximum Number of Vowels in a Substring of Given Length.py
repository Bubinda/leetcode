# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiouAEIOU'
        max_length = 0
        counter = 0
        for i in (s[i:i+k] for i in range(len(s)-(k-1))):
            for j in i:
                if j in vowels:
                    counter += 1
            max_length = max(max_length, counter)
            counter = 0 
        return max_length

        # -> exceed time limit but works


# follwing works better and is very efficient
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = 0
        current_count = 0
        
        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_vowels = current_count
        
        # Iterate through the rest of the string
        for i in range(k, len(s)): 
            if s[i] in vowels:
                current_count += 1 # here the current char is checked if this is a vowel +1
            if s[i - k] in vowels: # if the char k steps before is also a vowel the socre is reduced by one
                current_count -= 1
            max_vowels = max(max_vowels, current_count)
        
        return max_vowels