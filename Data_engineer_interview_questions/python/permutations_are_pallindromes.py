from collections import Counter

def is_palindrome_permutation(s):
    # Count the frequency of each character in the string
    char_counts = Counter(s)

    # Count the number of characters with odd frequencies
    odd_count = sum(count % 2 != 0 for count in char_counts.values())

    # For a palindrome permutation, at most one character should have an odd frequency
    return odd_count <= 1


# same with a dictionary
def is_palindrome_permutation_dict(s):
    char_counts = {}

    # Count the frequency of each character in the string
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Count the number of characters with odd frequencies
    odd_count = sum(count % 2 != 0 for count in char_counts.values())

    # For a palindrome permutation, at most one character should have an odd frequency
    return odd_count <= 1
