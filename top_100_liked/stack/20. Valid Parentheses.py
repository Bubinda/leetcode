# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {')':'(', ']': '[', '}': '{'}

        for element in s:
            if element in close_map:
                last_element = stack.pop() if stack else -1
                if close_map[element] != last_element:
                    return False
            else:
                stack.append(element)
            
        return not stack


# or with an open_map

class Solution(object):
    def isValid(self, s):
        open_map = {'(':')', '{':'}','[':']'}
        stack = []
        for element in s:
            if element in open_map:  
                stack.append(element)
            elif len(stack) == 0 or open_map[stack.pop()] != element: 
                return False
        return not stack