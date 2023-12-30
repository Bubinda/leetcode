# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

# does not work for negative numbers -> so the solution below does handle this problem by using a mask to ensure that the result stays within the range of 32-bit integers.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!= 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a



# This solution implements the bitwise operation approach to add two integers without using the + or - operators.

# The algorithm starts by initializing a mask variable to 0xFFFFFFFF which is used to ensure that the result stays within the range of 32-bit integers.

# Then, using a while loop, the algorithm applies two bitwise operations on a and b until b becomes 0:

# (a ^ b) & mask: This operation performs the bitwise exclusive OR (^) operation on a and b and then bitwise ANDs (&) the result with the mask variable to ensure that the result stays within the range of 32-bit integers. The result is then stored in a.

# ((a & b) << 1) & mask: This operation performs the bitwise AND (&) operation on a and b, then left shifts the result by 1 bit (<< 1), and finally bitwise ANDs (&) the result with the mask variable to ensure that the result stays within the range of 32-bit integers. The result is then stored in b.

# The above two operations are repeated until b becomes 0, at which point the value of a is returned as the sum of the original a and b values.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)





# use the log and exp functions to cnacel out each other and getting a plus operation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 and b != 0:
            return b
        elif b == 0 and a != 0:
            return a
        
        return int(log(exp(a) * exp(b)))