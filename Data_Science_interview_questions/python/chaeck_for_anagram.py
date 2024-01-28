# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the letters exactly once. For example, the words “anagram” and “nagaram” are anagrams.

# Problem description: Given two strings a and b, return True if b is an anagram of a, and False otherwise.



def is_anagram(a: str, b: str) -> bool:
    # first check the length if they are not the same they cannot be anagrams
    if len(a) != len(b):
        return False
    
    a = a.lower()
    b = b.lower()

    a_counter, b_counter = {}, {}

    for i,j in zip(a,b):
        if i not in a_counter:
            a_counter[i] = 1
        else:
            a_counter[i] += 1

        if j not in b_counter:
            b_counter[j] = 1
        else:
            b_counter[j] += 1

    return a_counter == b_counter


for words in [('apple', 'pale'), ('knee', 'keen'), ('listen', 'silent')]:
    print(f"Words {words[0]} and {words[1]} are anagrams? {is_anagram(a=words[0], b=words[1])}")