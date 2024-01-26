# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
#using a dictionary approach would use O(n) space complexity
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        majority = None
        max_count = 0
        for num, count in count_dict.items():
            if count > max_count:
                majority = num
                max_count = count

        return majority


# but if we only use a counter var we ca n do the same in O(1) space complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1

        return majority
    


# or a bit more compact

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0

        for i in nums:
            if count == 0:
                maj = i
                
            count += 1 if i == maj else -1

        return maj