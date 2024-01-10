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


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        #we wlak over our input list of words
        for word in strs:
            # each single word is sorted so it can be compared to the anagram keys
            sorted_word = ''.join(sorted(word))
            # is a word is not included in the anagram dictionary, we add an empty list 
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            # either way if the word is included or not the new word is appended to the list that is mapped to the sorted word key
            anagrams[sorted_word].append(word)
        # in the end all values of the hasmap are converted into a list, becuase those values are also lists, we gat a list of lists
        result = list(anagrams.values())
        
        return result
    



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            x = ''.join(sorted(i))
            if x in hashmap:
                hashmap[x].append(i)
            else:
                hashmap[x] = [i]
        
        return [i for i in hashmap.values()]



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            hashmap[key].append(s)
        
        return [i for i in hashmap.values()]