# Problem description: Given a positive integer x, return an integer that is a factorial of x. If a negative integer is provided, return -1. Implement the solution by using a recursive function.


def factorial_recursive(x: int) -> int:

    if x < 0: return -1
    if x == 0: return 1

    if x == 1: return x
    else:
        return x * factorial_recursive(x-1)
    


for x in [5, 7, 10, 12, 0, -3]:
    print(f"{x}! = {factorial_recursive(x=x)}")



    