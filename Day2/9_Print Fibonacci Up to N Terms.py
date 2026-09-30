# Print Fibonacci Up to N Terms

# Given an integer n, return an array of the first n Fibonacci numbers, starting from 0, 1, 1, 2, 3, 5, and so on.

# Each term after the first two is the sum of the two terms before it. If n is 0 or negative, return an empty array.

# Example 1:
# Input: n = 5

# Output: [0,1,1,2,3]

# Example 2:
# Input: n = 1

# Output: [0]

# Constraints:
# 0 <= n <= 90.
# n can be 0, which produces an empty array.


# Approach 1: Two-Variable Iteration


class Solution:
    def fibonacci(self, n: int) -> list[int]:
        ans = []
        prev, curr = 0, 1
        for _ in range(n):
            ans.append(prev)
            prev, curr = curr, prev + curr
        return ans

# Complexity Analysis

# Time Complexity: O(n). The loop runs exactly n times, producing one term per iteration with constant work each step.
# Space Complexity: O(n) for the result array, which holds all n terms. Beyond the output, only the two rolling variables are used, so the extra space is O(1).
    

# Intuition
# Each term depends only on the two terms before it, so two variables are enough: one for the previous term and one for the current term.

# Hold prev = 0 and curr = 1, the first two terms. On each step, append prev to the result, then advance the pair so that the new prev is the old curr and the new curr is the sum prev + curr. Appending prev first makes the seeds come out in order: the first append emits 0, the second emits 1, and from there each appended value is the sum computed one step earlier. Appending before advancing means n = 1 emits only the 0 and stops, with no special handling.

# Algorithm
# Create an empty list to hold the result.
# Set prev = 0 and curr = 1.
# Repeat n times: append prev to the list, then set prev, curr = curr, prev + curr.
# Return the list as an array.