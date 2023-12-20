# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        zero_counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1

            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1

            max_ones = max(max_ones, i+1-left)
        return max_ones
    


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, num_zeros, l = 0 

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            length = r - l + 1
            max_len = max(max_len, length)
            
        return max_len