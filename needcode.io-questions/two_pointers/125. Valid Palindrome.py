# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [a.lower() for a in s if a.isalpha() or a.isdigit()]
        left = 0
        right = len(s)-1

        if not s:
            return True
        else:
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue

                else:
                    return False
            
        return True

# way shorter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and remove non-alphanumeric characters
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

        # Check if the cleaned string is equal to its reverse
        return cleaned_s == cleaned_s[::-1]