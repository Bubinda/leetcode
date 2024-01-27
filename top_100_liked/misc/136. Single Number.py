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
 


# the idea behind this solution is that if you combine two same numbers with XOR the result will be 0
# Since there is only one number in the aaray that appears only one time, if the whole array is mapped together by XOr this single number will be the result of the mapping

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
    
# this process can also be doen be using the reduce method and a lambda function

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # the first input to the reduce funtion is the method that should be applied to the secodn input, which is in this case the nums array
        # this reduce method could be also used like this:
        # reduce(xor, nums) if the import: (import operator.xor as xor) is used to get the xor functionallity
        return reduce(lambda x, y: x ^ y, nums)

