# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



# solving it with Kadanes algorithm#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum
    


# personally i like this solution a bit more becuase it is more intuitive in my mind
class Solution:
    def maxSubArray(self, nums):
        max_sum_until_i = max_sum= nums[0]
        for i, num in enumerate(nums[1:],start=1):
            max_sum_until_i = max(max_sum_until_i+num, num)
            max_sum = max(max_sum,max_sum_until_i,max_sum)
        return max_sum
    

# my first solution was way slower but also somewhat similar from the core idea 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        max_with_end_on_current = 0
 
        for i in range(0, len(nums)):
            max_with_end_on_current = max_with_end_on_current + nums[i]
            if (max_value < max_with_end_on_current):
                max_value = max_with_end_on_current
 
            if max_with_end_on_current < 0:
                max_with_end_on_current = 0
        return max_value