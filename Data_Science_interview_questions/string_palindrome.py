# test input = „paul“

# output -> false


# two pointer solution

def palin_checker(text: str):
	first,last = 0,len(text)-1
	text = text.lower()

	while first <= last:
		if text[first] == text[last]:
			first += 1
			last -= 1

		return False

	return True




# if the text has other chars than alphanumeric ones, those should be cleaned


import re

def is_palindrome(text):
    # lowering the string
    text = text.lower()
   
    # Cleaning the string
    rx = re.compile('\W+')
    text = rx.sub('',text).strip()
   
    # Reversing and comparing the string
    return text == text[::-1]


# or like this

def is_palindrome(text):
    # lowering the string
    text = text.lower()
   
    # Cleaning the string
    rx = re.compile('\W+')
    text = rx.sub('',text).strip()
   
    # Reversing the string
    rev = ''.join(reversed(text))
    return text == rev





# another solution
# Problem description: Given a string s, return True if it’s a palindrome, or False otherwise.

import string
def is_palindrome(s: str) -> bool:
    # Lowercase the string 
    s = s.lower()
    
    # All lowercase letters and digits
    allowed = [*string.ascii_lowercase, *string.digits]
    
    # Remove non-alphanumeric characters
    s_fixed = ''
    for letter in s:
        if letter in allowed:
            s_fixed += letter
            
    s_reversed = ''
    # For every letter
    for letter in s_fixed:
        # Reversed string = letter + reversed string
        s_reversed = letter + s_reversed
        
    # Check for equality
    if s_fixed == s_reversed:
        return True
    return False


# Test cases
for word in ['Bob', '**Bob****', 'Appsilon', 'A man, a plan, a canal: Panama']:
    print(f"Is {word} a palindrome? {is_palindrome(s=word)}")



# recursive solution

def recursive_palindrome(text: str) -> bool:
     if len(text) <= 1:
          return True
     
     if text[0] == text[-1]:
          return recursive_palindrome(text[1:-1])
     
     return False

