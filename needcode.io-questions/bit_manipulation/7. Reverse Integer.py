# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            res=int(str(x)[::-1])
        else:
            res=int("-"+str(abs(x))[::-1])
        if res>=-(2**31) and res<=(2**31-1):
            return res
        else:
            return 0
        

class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        return ans if -2**31 <= ans < 2**31 else 0

