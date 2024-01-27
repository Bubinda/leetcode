# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0

        for i in nums:
            if count == 0:
                maj = i
                
            count += 1 if i == maj else -1

        return maj
    

# using the sorting method for this problem
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # this will return the elemnt at the n//2 index which is in a sorted array the element the one that appears more then the other
        return nums[n//2]
    


# using a hashmap (this does use extra space which does not fullfill the follow-up constraint of using O(1) extra space)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            d[num] += 1
        
        n = n // 2
        for key, value in d.items():
            if value > n:
                return key
            
        # alternate to the code above this code can be used to sort the dictionary by the values (so the most counted one is at first) and turns this into a list of key,value pairs 
        # so we index to the first value of the first element

        #sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse = True)
        #return sorted_dict[0][0]
            
        return 0