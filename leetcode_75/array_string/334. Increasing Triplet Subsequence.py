# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        min1 = float('inf')  # Initialize min1 to positive infinity
        min2 = float('inf')  # Initialize min2 to positive infinity

        for i in nums:
            if i <= min1:
                min1 = i
            elif i <= min2:
                min2 = i
            else:
                return True  # Found a triplet (min1 < min2 < num)

        return False  # No such triplet found