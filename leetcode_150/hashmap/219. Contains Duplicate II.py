# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


#works partially
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0,k+1

        while right <= len(nums):
            if len(set(nums[left:right])) != len(nums[left:right]):
                return True
            left += 1
            right += 1
        return False

    
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}  # Dictionary to store the most recent index for each number

        for i, num in enumerate(nums):
            # If the number has been seen before and the difference in indices is less than or equal to k, return True
            if num in num_to_index and i - num_to_index[num] <= k:
                return True
            # Update the most recent index for the number
            num_to_index[num] = i

        return False  # If no such pair of indices is found, return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}
        n = len (nums)

        for i in range (n):
            if nums[i] in num_to_i:
                if abs(num_to_i[nums[i]] - i) <= k:
                    return True
            num_to_i[nums[i]] = i
        
        return False