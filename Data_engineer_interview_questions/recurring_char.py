# Given a string, write a function recurring_char to find its first recurring character. Return None if there is no recurring character.

# Treat upper and lower case letters as distinct characters.

# You may assume the input string includes no spaces.

# Example 1:

# Input:

# input = "interviewquery"
# Output:

# output = "i"
# Example 2:

# Input:

# input = "interv"
# Output:

# output = None


def recurring_char(string):
    dict = {}
    for i in string:
        dict[i] = dict.get(i,0)+1
        if dict[i] > 1:
            return i
    return None


# alternative

def recurring_char_2(string):
    for i in range(len(string)):
        if string[i] in string[i+1 :]:
            return string[i]
    return 'None'



import timeit


# Set up input data or any necessary variables
string = "abcdefghijklmnopqrstuvwxyza" # on this string the secodn function is much faster
#but
string = "abcdefghijklmnopqrstuvwxyzz" # on this string the first function is as fast as on the first string but the second one is slower

# Measure the execution time of function 1
time_function_1 = timeit.timeit(lambda: recurring_char(string), number=1000)

# Measure the execution time of function 2
time_function_2 = timeit.timeit(lambda: recurring_char_2(string), number=1000)

# Compare the execution times
print(f"Execution time for function 1: {time_function_1:.5f} seconds")
print(f"Execution time for function 2: {time_function_2:.5f} seconds")

# Optionally, compare the relative speed
if time_function_1 < time_function_2:
    print("Function 1 is faster.")
elif time_function_1 > time_function_2:
    print("Function 2 is faster.")
else:
    print("Both functions have similar execution times.")

