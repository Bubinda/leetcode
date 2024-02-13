# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, path):
            if left == 0 and right == 0:
                res.append(''.join(path))
                return
            if left > 0:
                path.append('(')
                dfs(left - 1, right + 1, path)
                path.pop()
            if right > 0:
                path.append(')')
                dfs(left, right - 1, path)
                path.pop()

        res = []
        dfs(n, 0, [])
        return res








class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        ret = []

        def backtrack(num_open, num_close):
              if num_open == num_close == n:
                    ret.append(''.join(sol))
                    return
              
              if num_open < n:
                    sol.append('(')
                    backtrack(num_open + 1, num_close)
                    sol.pop()
              if num_close < num_open:
                    sol.append(')')
                    backtrack(num_open, num_close + 1)
                    sol.pop()
                    
        backtrack(0, 0)
        return ret































