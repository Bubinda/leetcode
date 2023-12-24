# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0  # To store the maximum length of the substring
        max_count = 0   # To store the count of the most frequent character in the current window
        start = 0       # Start of the sliding window

        # Create a list to store the count of each character
        char_dict = {}

        for end in range(len(s)):
            # Update the count of the character at the end of the window
            if s[end] not in char_dict:
                char_dict[s[end]] = 1
            else:
                char_dict[s[end]] += 1

            # Update max_count to keep track of the most frequent character
            max_count = max(max_count, char_dict[s[end]])

            # Calculate the number of extra operations required
            sub_length = end - start + 1 - max_count

            # If the number of extra operations is greater than k, shrink the window
            if sub_length > k:
                char_dict[s[start]] -= 1
                start += 1

            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)

        return max_length
    


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        my_max = 0
        l = 0

        for r in range(len(s)):
            arr[ord(s[r]) - ord('A')] += 1
            w_len = r - l + 1
            m = max(arr)

            while(w_len - m) > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
                w_len -= 1
                m = max(arr)

            my_max = max(my_max, w_len)

        return my_max
        