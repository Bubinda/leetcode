# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n 
        
        fib1, fib2 = 0,1

        for i in range(n-1):
            temp = fib2
            fib2 = fib1 + fib2
            fib1 = temp

        return fib2
    

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n 
        fib_array = [0, 1] + [0]*(n-1) 
        for i in range(2, n+1): 
            fib_array[i] = fib_array[i-1] + fib_array[i-2] 
        return fib_array[n] 