# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

#works but in worst case is m*n time complexity O(n*m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for i in stones:
            if i in jewels: jewels_count += 1
        
        return jewels_count
    


# better with O(n+m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        jewels = set([i for i in jewels]) #set lookup is O(1) instead of O(n) for a list
        for i in stones:
            if i in jewels: jewels_count += 1
        
        return jewels_count
    