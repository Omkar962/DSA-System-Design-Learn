# Count Digits in an Integer

# Given an integer n, return the number of digits in n.

# Count the digits of the absolute value, so the sign of a negative number does not count. The number 0 has 1 digit.

# Example 1:
# Input: n = 12345

# Output: 5

# Example 2:
# Input: n = -789

# Output: 3

# Constraints:
# -2^31 <= n <= 2^31 - 1
# n may be negative, zero, or positive.


# Approach 1: Repeated Division

class Solution:
    def countDigits(self, n: int) -> int:
        # Zero is written as a single symbol, so it has 1 digit
        if n == 0:
            return 1
        # Work on the absolute value so the loop counts the same digits
        n = abs(n)
        count = 0
        # Each division by 10 removes one digit
        while n != 0:
            n //= 10
            count += 1
        return count
# Complexity Analysis

# Time Complexity: O(d), where d is the number of digits in n. Since the digit count grows with the logarithm of the value, this is O(log n). The loop runs once per digit.
# Space Complexity: O(1). The counter is the only extra storage, and its size does not depend on n.


class Solution:
    def countDigits(self, n: int) -> int:
        # The string of the absolute value contains only digit characters
        return len(str(abs(n)))

# Complexity Analysis

# Time Complexity: O(d), where d is the number of digits in n. Building the string and measuring its length both scale with the digit count, which is O(log n).
# Space Complexity: O(d). The string holds one character per digit, so its size grows with the number of digits.