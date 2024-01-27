# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# two pointer solution 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # rotate the whole array
        reverse(0, len(nums) - 1)
        # rotate all elements up to the k-th one
        reverse(0, k - 1)
        # roate all element from the k-th to the end
        reverse(k, len(nums) - 1)



# solution by slicing the array
def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if l == k: return

        k = k%l
        nums[:] = nums[-k:] + nums[:-k]



# using a loop 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)

        # also a different approach using a loop -> should be more time efficient as we do not use the insert at postion 0 which does shift the whole array (element by element) one step to the right
        # but both of those approaches are not very time efficient for large arrays
        # for i in range(k,0,-1):
        #     a=nums[-1]
        #     nums[:] = [a] + nums[:-1]