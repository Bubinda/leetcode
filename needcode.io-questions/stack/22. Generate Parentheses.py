# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


def generateParenthesis(n):

    stack = []
    solution = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            solution.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    backtrack(0, 0)
    return solution



# without a stack but also backtrack, maybe a little bit more understanable
def generateParenthesis(self, n: int) -> List[str]:
	def dfs(left, right, s):
		if len(s) == n * 2:
			res.append(s)
			return 

		if left < n:
			dfs(left + 1, right, s + '(')

		if right < left:
			dfs(left, right + 1, s + ')')

	res = []
	dfs(0, 0, '')
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