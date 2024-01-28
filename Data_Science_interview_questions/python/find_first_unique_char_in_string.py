# Problem description: Given a string s, find the first non-repeating character and return its index. If it doesn’t exist, return -1.


def find_first(text: str) -> int:
    chars = {}

    text = text.lower()

    for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    for char, i in chars.items():
        if i == 1:
            return text.index(char)
    
    return -1




text = "helloezhowareyou"
print(find_first(text))




def first_unique_character(s: str) -> int:
    # Lowercase
    s = s.lower()
    # Dictionary storing individual letters and their counts
    counts = {}
    # For every letter in the string
    for letter in s:
        # If letter not in dictionary, add it and set the count to 1
        if letter not in counts:
            counts[letter] = 1
        # If letter in dictionary, add 1 to the count
        else:
            counts[letter] += 1
        # For the range of string length
    for i in range(len(s)):
        # If there's only one letter
        if counts[s[i]] == 1:
        # Return the index position
            return i
    # No first unique character
    return -1

# Test cases
for s in ['Appsilon', 'Appsilon Poland', 'abcabc']:
    print(s)
    print(f"Index: {first_unique_character(s=s)}")
    print(f"Index: {find_first(text=s)}")
    print("---")
