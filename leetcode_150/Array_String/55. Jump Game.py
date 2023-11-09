# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = nums[0]
        if nums[0] == 0 and len(nums)!=1:
            max_index = 0
            return False
        
        for i in range(1,len(nums)-1):
            if nums[i] > 0:
                max_index = max(max_index, i+nums[i])
            if nums[i] == 0 and max_index<i+1:
                return False

        return max_index >= len(nums)-1


# a bit simpler
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return max_reach >= len(nums) - 1


 # by using dynamic programming:
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        return dp[n - 1]