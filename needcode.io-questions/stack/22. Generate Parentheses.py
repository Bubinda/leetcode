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

    # for a type of task where different combinations of elements are required a backtrack might be a good approach
    # we give the function the number of open and closed parenthesis as input
    def backtrack(openN, closedN):
        # base case:
        # if the number of open and clsed parenthesis are the same and also equal to the number of required elements we append our stack to the solution array and the return
        if openN == closedN == n:
            solution.append("".join(stack))
            return
        # if the number of open parenthesis are smaler than required number of open parenthesis
        if openN < n:
            # we first append an open parenthesis to the stack
            stack.append("(")
            # then call the backtrack function on the new number of parenthesis
            backtrack(openN + 1, closedN)
            # and in the end reverse the changes made to the stack
            stack.pop()
            # the removing is done to get the path split in the backtracking "tree" where we always have two paths from one parent. 
            # precisely we can always decide to add a parenthese or we do not add one
        # if the number of clodes ones is larger than opened ones, we need to close some
        if closedN < openN:
            # so we decide to add a closing one
            stack.append(")")
            # call the backtrack
            backtrack(openN, closedN + 1)
            # and then decide to not add one by the pop
            stack.pop()
    # to start our backtrack we need to call the function with 0 open and 0 clsing parenthsis
    backtrack(0, 0)
    # in the end we return our solution with all the permutations of n valid clsoing and opening parenthesis
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