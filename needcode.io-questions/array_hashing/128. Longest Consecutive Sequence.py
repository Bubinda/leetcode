# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums) # needs to be a set to check the general streak, for this duplicates are irrelevant
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # Check if the number is the start of a sequence
                current_streak = 1
                
                while num + current_streak in num_set:  # Extend the sequence
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak