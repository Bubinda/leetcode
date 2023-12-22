# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            # Helper function to calculate the sum of the squares of digits
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
            return total_sum

        seen = set()  # To detect cycles
        while n != 1:
            if n in seen:
                return False  # Cycle detected
            seen.add(n)
            n = get_next(n)

        return True  # If n reaches 1, it's a happy number
    

# more user-friendly - easy to read but runs slightly slower than the solution above
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            summ = 0
            for digit in cur:
                digit = int(digit)
                summ += digit ** 2
            
            if summ == 1: return True

            cur = str(summ)
        
        return False