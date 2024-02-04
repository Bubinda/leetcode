# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        i = 0 
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
                
            i += 1
        return strs[0][:i]
    


class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        # Sort the input list v lexicographically. This step is necessary because the common prefix should be common to all the strings, so we need to find the common prefix of the first and last string in the sorted list.
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 