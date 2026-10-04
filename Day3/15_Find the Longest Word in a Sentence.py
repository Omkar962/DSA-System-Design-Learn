# Find the Longest Word in a Sentence

# Given a sentence s made of words separated by spaces, return the longest word in the sentence. The answer is the word itself, not its length or its position.

# If two or more words share the longest length, return the first one that reaches that length. Extra spaces between words should not produce an empty word as the answer.

# Example 1:
# Input: s = "I love programming languages"

# Output: "programming"

# Example 2:
# Input: s = "the quick brown fox"

# Output: "quick"

# Constraints:
# 1 <= s.length <= 1000
# The sentence contains at least one word.
# Words are separated by spaces.


# Approach 1: Two Pointers single pass


# Algorithm
# Track the start index and length of the current word, plus the best start index and best length found so far.
# Walk through the string one character at a time, going one step past the end so the final word is closed off.
# When you see a non-space character, extend the current word length, marking the start if it is the first character of the word.
# When you see a space or reach the end, the current word is complete, so update the best word if the current word is strictly longer, then reset the current word.
# After the scan, build the answer from the best start index and best length.

class Solution:
    def longest_word(self, s: str) -> str:
        best_start, best_len = 0, 0
        cur_start, cur_len = 0, 0
        # Loop one past the end so the last word gets closed
        for i in range(len(s) + 1):
            if i < len(s) and s[i] != ' ':
                if cur_len == 0:
                    cur_start = i
                cur_len += 1
            else:
                if cur_len > best_len:
                    best_len = cur_len
                    best_start = cur_start
                cur_len = 0
        return s[best_start:best_start + best_len]

# Time & Space Complexity
# Time Complexity: O(n). The scan visits each character once, and slicing out the best word at the end costs at most the length of that word.
# Space Complexity: O(1) beyond the output. Only a handful of index counters are kept, with no list of words allocated. The returned substring itself is the only sizable allocation.