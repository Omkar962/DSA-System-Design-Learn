# Palindrome String Check

# Given a string s made of lowercase alphanumeric characters, return true if it reads the same forward and backward, and false otherwise.

# The input is already lowercase with no spaces or punctuation, so the characters can be compared directly. An empty string and a single character both count as palindromes, since there is no mismatched pair.

# Example 1:
# Input: s = "racecar"

# Output: true

# Example 2:
# Input: s = "hello"

# Output: false

# Constraints:
# 0 <= s.length <= 1000
# The string contains only lowercase alphanumeric characters.

# Approach 1: Two Pointers

class Solution:
    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        # Compare mirrored characters moving inward
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Time & Space Complexity
# Time: O(n) — one pass through the string
# Space: O(1) — only two variables are used




# Count Words in a Sentence

# Given a string s, count the number of words it contains. A word is a contiguous run of non-space characters, and words are separated by one or more spaces.

# Handle leading spaces, trailing spaces, and multiple spaces between words correctly. An empty string or a string of only spaces contains zero words.

# Example 1:
# Input: s = "hello world"

# Output: 2

# Example 2:
# Input: s = "  leading and trailing  "

# Output: 3

# Constraints:
# 0 <= s.length <= 10^4
# s consists of printable ASCII characters, including spaces.


# Approach 1: Split and Count

class Solution:
    def countWords(self, s: str) -> int:
        list_str=s.split()
        return len(list_str)

# Time & Space Complexity
# Time: O(n) — one pass through the string to split it into words
# Space: O(n) — space used to store the list of words