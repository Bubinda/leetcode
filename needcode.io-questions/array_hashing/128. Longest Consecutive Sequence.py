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
        
        # needs to be a set to check the general streak, for this duplicates are irrelevant
        num_set = set(nums) 
        longest_streak = 0
        
        # we iterate over all numbers in the number set
        for num in num_set:
            # Check if the number is the start of a sequence
            if num - 1 not in num_set:  
                current_streak = 1
                
                # if we have found a new (or potentially new) start of our streak we add the current streak (which is increased in each iteration) to our current number
                while num + current_streak in num_set:  # Extend the sequence
                    current_streak += 1
                # after we have run over the while loop we update our longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
    



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in s:
                current_len = 1 
                next_num = num + 1
                while next_num in s:
                    current_len += 1
                    next_num += 1
                max_len = max(current_len, max_len)

        return max_len