# Sum of All Divisors of a Number


# Given a positive integer n, return the sum of all of its divisors, including 1 and n itself.

# A divisor of n is any positive integer that divides n with no remainder. For example, the divisors of 12 are 1, 2, 3, 4, 6, 12, and their sum is 28.

# Example 1:
# Input: n = 12

# Output: 28

# Example 2:
# Input: n = 6

# Output: 12

# Constraints:
# 1 <= n <= 10^6.
# The sum fits in a 32-bit integer at this range, but use a 64-bit accumulator to stay safe against larger inputs.

#Approach 1: Linear Scan

class Solution:
    def sumOfDivisors(self, n: int) -> int:
        # Python integers grow as needed, so there is no overflow to manage
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i
        return total

# Complexity Analysis

# Time Complexity: O(n). The loop runs once for each value from 1 to n, performing one modulo check each time.
# Space Complexity: O(1). Only the running sum is stored, regardless of how large n is.



#Approach 2: Scan to Square Root

# Divisors come in pairs. If i divides n, then n / i divides n too. For n = 12, 2 pairs with 6, and 3 pairs with 4. One member of each pair is at most the square root of n and the other is at least the square root, so scanning only up to the square root finds both members of every pair.

# Loop i while i * i <= n. Whenever i divides n, add both i and its partner n / i. One detail needs care: when n is a perfect square, i equals n / i at the middle, so add that divisor only once to avoid counting it twice.

# Algorithm
# Initialize an accumulator sum to 0.
# Loop i starting at 1 while i * i <= n.
# If n % i equals 0, then i is a divisor:
# Add i to sum.
# Compute the partner n / i. If it differs from i, add it to sum as well. If it equals i, skip it so the perfect-square divisor is not double counted.
# After the loop ends, return sum.

class Solution:
    def sumOfDivisors(self, n: int) -> int:
        # Each divisor i below the square root pairs with n // i above it
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                total += i
                pair = n // i
                # Add the partner only when it is a different value
                if pair != i:
                    total += pair
            i += 1
        return total

# Complexity Analysis

# Time Complexity: O(sqrt n). The loop stops once i passes the square root of n, so it runs about sqrt(n) times instead of n times.
# Space Complexity: O(1). The running sum and a single pair variable are the only storage used.