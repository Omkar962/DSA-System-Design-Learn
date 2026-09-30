# Prime Number Check

# Given an integer n, return true if n is a prime number and false otherwise.

# A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself. Any value of 1 or less, including 0 and negative numbers, is not prime.

# Example 1:
# Input: n = 17

# Output: true

# Example 2:
# Input: n = 18

# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1
# n may be negative, zero, or positive.

# Approach 1: Trial Division up to n-1

class Solution:
    def isPrime(self, n: int) -> bool:
        # Primality is only defined for integers greater than 1
        if n <= 1:
            return False
        # Any divisor between 2 and n-1 makes n composite
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
# Complexity Analysis

# Time Complexity: O(n). The loop tests every candidate from 2 up to n - 1, so the work grows linearly with the value of n.
# Space Complexity: O(1). Only the loop counter is stored, and its size does not depend on n.


# Approach 2: Trial Division up to √n

class Solution:
    def isPrime(self, n: int) -> bool:
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True

# Complexity Analysis

# Time Complexity: O(√n). The loop only runs candidates up to the square root of n, so the work scales with the square root of the value rather than the value itself.
# Space Complexity: O(1). Only the loop counter is stored, and its size does not depend on n.