# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums) <= k:
            return sum(nums)/k
        else:
            # we initialize the max_avg and the current usm as the sum of the input array from the start up to element with kth index        
            max_avg = curr_sum = sum(nums[:k])

        # then we run over our input array from index k up tot the end
        for i in range(k,len(nums)):
            # for each poition we subtrackt the first element and add the new (current element)
            curr_sum += nums[i] - nums[i - k]
            # then for each index we check if the new curr_sum is larger than the max_avg we have found so far
            max_avg = max(max_avg,curr_sum)
        # because the window size is always k we can divide by k in the end
        # previously we just tring to find the largest sum within the windows size of k
        return max_avg/k