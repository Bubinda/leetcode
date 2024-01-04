# Problem description: Given an integer n, return a string array result where:

# result[i] == “FizzBuzz” if i is divisible by 3 and 5.
# result[i] == “Fizz” if i is divisible by 3.
# result[i] == “Buzz” if i is divisible by 5.
# result[i] == i in any other case.
# You should check for the FizzBuzz condition first, as it checks for multiple conditions. For example, the number 15 is divisible with both 3 and 5, so FizzBuzz should get printed. 15 is also divisible by 3 and 5 individually, and we don’t want Fizz or Buzz printed alone.


def fizzbuzz(n: int) -> list:
    # To store the results
    arr = []
    # Iterate over range (1, n + 1)
    for num in range(1, n + 1):
    # FizzBuzz check (number divisible by both 3 and 5)
        if num % 3 == 0 and num % 5 == 0:
            arr.append('FizzBuzz')
            continue
        # Fizz check (number divisible only by 3)
        elif num % 3 == 0:
            arr.append('Fizz')
            continue
        # Buzz check (number divisible only by 5)
        elif num % 5 == 0:
            arr.append('Buzz')
            continue
        # Number not divisible by (3 and 5) or 3 or 5
        else:
            arr.append(str(num))
    return arr
# Test - N = (3, 5, 15)
for n in [3, 5, 15]:
    print(f"FizzBuzz(n={n}) = {fizzbuzz(n)}")
