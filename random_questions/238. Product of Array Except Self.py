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
    

# the following two only are using a single extra array instead of two for the solution above

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
    


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize the answer array with 1s
        answer = [1] * n
        
        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer