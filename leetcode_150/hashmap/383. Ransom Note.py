# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = {}
        magazine_count = {}

        for char in ransomNote:
            ransom_count[char] = ransom_count.get(char, 0) + 1

        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        for char, count in ransom_count.items():
            if char not in magazine_count or count > magazine_count[char]:
                return False

        return True



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        magazin_counter = Counter(magazine)

        solution = list(note_counter - magazin_counter)

        if solution == []:
            return True
        else:
            return False