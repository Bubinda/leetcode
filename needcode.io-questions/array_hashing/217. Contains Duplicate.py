# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counters = {}
        # for this task we run a loop over all numbers in our input list and then...
        for i in nums:
            # ... check for each number if it is already included in our hashmap
            if i in counters:
                # if this is true then we can return ture because we have found a duplicate
                return True
            else:
                # otherwise the current number is added to the hashmap with the value 1
                counters[i] = 1
        # if we ran our code unitl this point this means that there are no duplicetes included in the list
        return False
    
# the version below is the same as above but we do not use a hasmap but rather a set, which is as efficent as a hashmap because under the hood python uses also a hasmap as data stucture
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set()

        for i in nums:
            if i in set_num:
                return True
            else:
                set_num.add(i)
        return False



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counters = set()

        for i in nums:
            if i in counters:
                return True
            else:
                counters.add(i)
        return False



