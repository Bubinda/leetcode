# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

# does not work if same number is included two times in array
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            goal = target - value
            if goal in numbers[index+1:]:
                return [index+1,numbers.index(goal)+1]
            else:
                continue

#better use a two pointer approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high = len(numbers)-1
        low = 0
        while low<high:
            if numbers[low]+numbers[high] > target:
                high -=1
                continue
            if numbers[low]+numbers[high] < target:
                low +=1
                continue
            elif numbers[low]+numbers[high] == target:
                break
        return [low+1,high+1]

#second two pointer approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
        
        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]
            if current_sum == target:
                return [index1 + 1, index2 + 1]  
            elif current_sum < target:
                index1 += 1
            else:
                index2 -= 1
        return []