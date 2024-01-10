# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # we use a hashmap where the key is the closing bracket and the value is the opening bracket to check if the closing bracket is the correct one
        bracket_map = {')': '(', '}': '{', ']': '['}

        # we wlak over the input
        for char in s:
            # for each char in the input we check if it is a closing bracket of any type
            if char in bracket_map:
                # if it is we check if the stack is empty
                top_element = stack.pop() if stack else '#'
                # if the poped element (opening bracket) from the stack is not equal to the current closing bracket the input is not valid
                if bracket_map[char] != top_element:
                    return False
            # if we read an opening bracket we append it to the stack
            else:
                stack.append(char)
        # in the end we return if the stack is empty -> which means that the input was valid
        return not stack
    


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                if not stack: return False
                top_element = stack.pop()
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack