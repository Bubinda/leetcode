# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = []
        
        for i in range(1,n+1):
            curr = 0
            div_by_3 = i % 3 == 0
            div_by_5 = i % 5 == 0

            if div_by_3 and div_by_5:
                curr = "FizzBuzz"
            elif div_by_3:
                curr = "Fizz"
            elif div_by_5:
                curr = "Buzz"
            else:
                curr = str(i)
            
            sol.append(curr)

        return sol
    


class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(1, n + 1):
            ans.append(
                "FizzBuzz" if i % 15 == 0 else
                "Buzz" if i % 5 == 0 else
                "Fizz" if i % 3 == 0 else
                str(i)
            )
        return ans
    


