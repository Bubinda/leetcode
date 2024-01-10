# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we create variables for the langth of our input and an answer list which contains as many ones as the lnegth of the input
        n = len(nums)
        answer = [1] * n
        
        # first we make our run from left to right, to calculate our left product
        left_product = 1
        for i in range(n):
            # for this we multiply our current left_product to the element i in the answer array
            answer[i] *= left_product
            # then we update our current product by multiplying it by the element in the input array at positon i 
            left_product *= nums[i]
            # by this loop we always multiply the "previous" / left elemnt of the input array (nums) to the current result in our answer array
        
        # next we run the product from the right to the left to multply each right product to the previously claculated left product of the input array
        right_product = 1
        for i in range(n - 1, -1, -1):
            # the calculations are the same as before, we only run over our input array in the reversed way (right to left)
            answer[i] *= right_product
            right_product *= nums[i]

        
        return answer