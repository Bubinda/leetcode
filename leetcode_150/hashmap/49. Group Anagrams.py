# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrams = {}

        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in angrams:
                angrams[sorted_i] = [i]
            else:
                angrams[sorted_i].append(i)

        return list(angrams.values())

