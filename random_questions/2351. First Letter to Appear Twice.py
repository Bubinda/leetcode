# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:

# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.
 

# Example 1:

# Input: s = "abccbaacz"
# Output: "c"
# Explanation:
# The letter 'a' appears on the indexes 0, 5 and 6.
# The letter 'b' appears on the indexes 1 and 4.
# The letter 'c' appears on the indexes 2, 3 and 7.
# The letter 'z' appears on the index 8.
# The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
# Example 2:

# Input: s = "abcdd"
# Output: "d"
# Explanation:
# The only letter that appears twice is 'd' so we return 'd'.


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for char in s:
            if char in seen:
                return char
            else:
                seen.append(char)

# followup question would be if we shouldnt use a hashset?
# in this case this is not nessecary because our list does only contain at most 26 elements (all lowercase latters of the alphabet) and in such a small list the lookup would be seen as constant time O(1) 
# if the input would also contain uppercase letter and other symbols then the consideration of a hashset would make more sense

#this could also be done with a set, which should reduce the time complexity -> but whith the given constaints and the description above why a hashset would be overkill the change to a set from alist wouldnt make much of a difference
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            else:
                seen.add(char)