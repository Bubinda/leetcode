#first solution
import bisect

def left_insertion_point(sorted_list, value):
    index = bisect.bisect_left(sorted_list, value)
    return index



# second one with using binary search
def left_insertion_point(arr, target):
    """
    Find the left insertion point for a specified value in sorted order.

    Parameters:
    - arr (list): A sorted list of elements.
    - target: The value to find the left insertion point for.

    Returns:
    - int: The index at which the value should be inserted.
    """
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

# Example usage:
sorted_array = [1, 3, 5, 7, 9]
value_to_insert = 6

insertion_point = left_insertion_point(sorted_array, value_to_insert)
print(f"The left insertion point for {value_to_insert} is at index {insertion_point}")
