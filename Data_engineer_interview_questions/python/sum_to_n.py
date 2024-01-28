#BFS

from collections import deque

def sum_to_n_bfs(integers, N):
    result = []
    queue = deque([(N, [])])

    while queue:
        current_target, current_combination = queue.popleft()

        if current_target == 0:
            if sorted(current_combination) not in result:
                result.append(sorted(current_combination))
            continue

        for num in integers:
            if current_target - num >= 0:
                queue.append((current_target - num, current_combination + [num]))

    return result

# # Example usage:
# integers = [2, 3, 5]
# N = 8
# result = sum_to_n(integers, N)
# print(result)


#DFS


def sum_to_n_dfs(integers, N):
    result = []
    queue = list([(N, [])])

    while queue:
        current_target, current_combination = queue.pop()

        if current_target == 0:
            if sorted(current_combination) not in result:
                result.append(sorted(current_combination))
            continue

        for num in integers:
            if current_target - num >= 0:
                queue.append((current_target - num, current_combination + [num]))

    return result

# # Example usage:
# integers = [2, 3, 5]
# N = 8
# result = sum_to_n_dfs(integers, N)
# print(result)




#recursive

def sum_to_n(integers, N):
    result = []
    find_combinations(integers, N, [], result)
    return result

def find_combinations(integers, target, current_combination, result):
    if target == 0:
        result.append(current_combination.copy())
        return
    if target < 0 or not integers:
        return

    # Include the first integer in the current combination
    find_combinations(integers, target - integers[0], current_combination + [integers[0]], result)

    # Exclude the first integer and find combinations for the remaining list
    find_combinations(integers[1:], target, current_combination, result)

# # Example usage:
# integers = [2, 3, 5]
# N = 8
# result = sum_to_n(integers, N)
# print(result)






import timeit


# Set up input data or any necessary variables
integers = [2, 3, 5, 6,7,8,9,10,12,14,16,18]
N = 20

# Measure the execution time of function 1
time_function_1 = timeit.timeit(lambda: sum_to_n(integers, N), number=1000)

# Measure the execution time of function 2
time_function_2 = timeit.timeit(lambda: sum_to_n_dfs(integers, N), number=1000)

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