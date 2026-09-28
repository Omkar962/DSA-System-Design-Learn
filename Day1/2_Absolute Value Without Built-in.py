# Absolute Value Without Built-in

# Given an integer n, return its absolute value without using any built-in absolute value function (such as Math.abs, abs, or fabs).

# The absolute value of a number is its distance from zero, so it is always non-negative. For example, the absolute value of -5 is 5, and the absolute value of 5 is also 5.

# Example 1:
# Input: n = -5

# Output: 5

# Example 2:
# Input: n = 42

# Output: 42

# Constraints:
# -2^31 <= n <= 2^31 - 1
# The input fits in a 32-bit signed integer.


# Approach 1 = Conditional Negation

class Solution:
    def absolute_value(self, n: int) -> int:
        # Negate only when n is negative
        if n < 0:
            return -n
        return n

# Complexity Analysis

# Time Complexity: O(1). The function runs one comparison and at most one negation, regardless of the input value.
# Space Complexity: O(1). No extra storage beyond the input and return value.


# Approach 2 = Bit Manipulation

class Solution:
    def absolute_value(self, n: int) -> int:
        # Python ints are unbounded, but for 32-bit values n >> 31
        # still yields -1 for negatives and 0 otherwise, so the
        # same formula works across the test range.
        mask = n >> 31
        return (n ^ mask) - mask


# Complexity Analysis

# Time Complexity: O(1). The result comes from a fixed sequence of bitwise and arithmetic operations with no loop.
# Space Complexity: O(1). Only the mask variable is used in addition to the input and return value.


# Step 1: Compute the mask. -5 >> 31 copies the sign bit across all 32 positions, giving all 1 bits, which is -1. So mask = -1.

# Step 2: XOR n with mask. In 32-bit form, -5 is ...11111011. XORing with -1 (all 1 bits) flips every bit to ...00000100, which is 4. So n ^ mask = 4.

# Step 3: Subtract mask. 4 - (-1) = 4 + 1 = 5.

# The result is 5, the absolute value of -5.

# For a non-negative input like n = 42, the mask is 0. Then 42 ^ 0 = 42 and 42 - 0 = 42, leaving the value unchanged.