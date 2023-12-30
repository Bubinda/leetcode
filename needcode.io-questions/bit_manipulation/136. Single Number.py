# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


# this works the same as the soulution below it but uses the reduce function to reduce the list to a single value
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

# Intuition:
# Xor of any two num gives the difference of bit as 1 and same bit as 0.
# Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
# So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
    
# list [1, 2, 1, 3, 3, 4, 5, 4, 5] -> set {1, 2, 3, 4, 5}

# 2 * sum({1,2,3,4,5}) = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5

# sum([1,2,1,3,3,4,5,4,5]) = 1 + 1 + 2 + 3 + 3 + 4 + 4 + 5 + 5

# Subtracting one from the other will give you the element that is unique in the list. 
# The set allows us to double up every element. 
# When we subtract off the sum of the original elements, the doubled up elements cancel out and we are left with the unique element.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)