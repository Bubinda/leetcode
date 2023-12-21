# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        return s_dict == t_dict


# like the first one but written a little shorter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_range= len(s)
        if s_range!= len(t):
            return False
        count_s, count_t = {},{}

        for i in range(s_range):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for c in count_s:
            if count_s[c] != count_t[c]:
                return False
        return True
    
        # alternate
        # conut_s != count_t


# very simple

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

# very simple and as efficient as the first one
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {},{}
        if len(s) != len(t):
            return False
        
        for s_val,t_val in zip(s,t):
            if s_val not in hash_s: hash_s[s_val] = 1
            else: hash_s[s_val] += 1
            if t_val not in hash_t: hash_t[t_val] = 1
            else: hash_t[t_val] += 1

        return hash_s == hash_t
    



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = {}

        for c in s:
            f[c] += 1
        else:
            f[c] = 1
        
        for c in t:
            if c not in f: return False
            elif f[c] == 1: del f[c]
            else: f[c] -= 1
        
        return not f
