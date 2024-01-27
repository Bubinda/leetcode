# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_mult = 1
        left_arr = [0]*n

        right_mult = 1
        right_arr = [0]*n

        for i in range(n):
            j = -i -1

            left_arr[i] = left_mult
            left_mult *= nums[i]

            right_arr[j] = right_mult
            right_mult *= nums[j]

        return [l*r for l,r in zip(left_arr, right_arr)]
    

# more compact solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, pre, post = [1]*len(nums), 1, 1

        for i in range(len(nums)):

            ans[i] *= pre
            ans[-1-i] *= post
            pre, post = pre*nums[i], post*nums[-1-i]
        
        return ans
    


# double loop which could be a bit easier to understand
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n

        for i in range(n):

            result[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(n-1,-1,-1):

            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result