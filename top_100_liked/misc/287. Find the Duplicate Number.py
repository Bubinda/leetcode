# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3


#slow and fast pointer approach, this does fullfill all the given requeirements, but is a bit complex to understand
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
    


# set /hash solution -> does use extra space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# counter solution -> does also use extra space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = [0] * (len(nums) + 1)
        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return num
        return len(nums)
    

# sort solution -> modifies the original array and also is not the most time efficient solution through the sorting

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return len(nums)