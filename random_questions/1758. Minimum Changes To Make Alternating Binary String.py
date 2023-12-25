# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

 

# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
 

class Solution:
    def min_operations(self, s: str) -> int:
        role_number_one = 0
        role_number_two = 0
        n = len(s)

        if n % 2 == 1:
            if s[n - 1] == '1':
                role_number_two += 1
            else:
                role_number_one += 1

        for i in range(0, n - 1, 2):
            if s[i] != '1' and s[i + 1] != '0':
                role_number_one += 2
            if s[i] == '1' and s[i + 1] != '0':
                role_number_one += 1
            if s[i] != '1' and s[i + 1] == '0':
                role_number_one += 1

            if s[i] != '0' and s[i + 1] != '1':
                role_number_two += 2
            if s[i] != '0' and s[i + 1] == '1':
                role_number_two += 1
            if s[i] == '0' and s[i + 1] != '1':
                role_number_two += 1

        return min(role_number_one, role_number_two)
    


class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        
        return min(start0, start1)
