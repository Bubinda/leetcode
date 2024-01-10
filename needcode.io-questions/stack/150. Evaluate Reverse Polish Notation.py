# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # we save our operatore of the equation in a list to check for them
        operands = ['+', '-', '*', '/']

        # we are looping ov er our input list
        for i in tokens:
            # if we encounte a number and no operator we append this to our stack
            if i not in operands:
                stack.append(int(i))
            # if we get an operator in the list
            else:
                # we create a local results variable
                result = 0
                # then we get our lates two numbers (the two which are left from the operator and by this the ones that sholud be computetd by this operator)
                num2 = stack.pop()
                num1 = stack.pop()
                # we check which operator we got and compute the result 
                if i == '+':
                    result = num1+num2
                elif i == '-':
                    result = num1-num2
                elif i == '*':
                    result = num1*num2
                # special case for the division if we encounter a division by 0
                else:
                    # Handle integer division by zero
                    if num1 * num2 < 0 and num1 % num2 != 0:
                        result = num1 // num2 + 1
                    else:
                        result = num1 // num2
                # the result is appended as a new number to the stack
                stack.append(result)
        # in the end the fianl result is stored as the only number in the stack at position 0
        return stack[0] 


from math import ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                b,a = stk.pop(), stk.pop()
                if t == '+':
                    stk.append(a+b)
                elif t == '-':
                    stk.append(a-b)
                elif t == '*':
                    stk.append(a*b)
                else:
                    div = a / b
                    if div < 0:
                        stk.append(ceil(div)) 
                    else:
                        stk.append(int(div))
                
            else:
                stk.append(int(t))

        return stk[0]