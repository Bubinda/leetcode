# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        # we are going over all our numbers in the input list
        # we use enumerate in this way we can get the index of the number as well as the number itself 
        for index, num in enumerate(nums):
            # we calculate the complement number to our current number
            complement = target - num
            # if the complent is already included in our hashmap
            if complement in num_indices:
                # then we return our current index and the value that is set in the hashmap for the corresponding complemnt number
                return [num_indices[complement], index]
            # if the complent value is not in our hashmap then we us the number as a key and the index of this number as the value
            num_indices[num] = index
        # if we do not find the complemnt of the number we return an empty list, but the requirements do state that there is always a solution
        return []



