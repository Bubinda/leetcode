# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
 

# Example 1:

# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# Example 2:

# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.


# works but very slow
class Solution:
    def removeStars(self, s: str) -> str:
        while '*' in s:
            # find the first star
            star_idx = s.index('*')
            # find the closest non-star char to the left
            non_star_idx = star_idx - 1
            while non_star_idx >= 0 and s[non_star_idx] == '*':
                non_star_idx -= 1
            # remove the star and the closest non-star char
            s = s[:non_star_idx] + s[star_idx + 1:]
        return s


#much faster
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []  # Use a stack to keep track of non-star characters
        result = []

        for char in s:
            if char == '*':
                # If a star is encountered, remove the closest non-star character from the stack
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        # Convert the stack to a string to get the final result
        return ''.join(stack)