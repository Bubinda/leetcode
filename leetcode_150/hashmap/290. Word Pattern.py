# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = [i for i in s.split()]
        pattern_dict = {}

        if len(s_list) != len(pattern):
            return False

        for i,j in zip(pattern,s_list):
            if i not in pattern_dict and j not in pattern_dict.values():
                pattern_dict[i] = j
            elif i not in pattern_dict and j in pattern_dict.values():
                return False
            else:
                if pattern_dict[i] != j:
                    return False
        return True



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        used_words = set()
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in pattern_to_word:
                if pattern_to_word[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in used_words:
                    return False
                pattern_to_word[pattern[i]] = words[i]
                used_words.add(words[i])
        
        return True