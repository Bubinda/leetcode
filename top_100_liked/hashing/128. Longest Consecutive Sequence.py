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
        if not nums: return 0

        max_sequence = 1
        nums_set = set(nums)

        for number in nums_set:
            if number - 1 not in nums_set:
                current_seq_length = 1

                while number + current_seq_length in nums_set:
                    current_seq_length += 1

                max_sequence = max(max_sequence, current_seq_length)

        return max_sequence




