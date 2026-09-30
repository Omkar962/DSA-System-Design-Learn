# Print All Primes Up to N

# Given an integer n, return an array of all prime numbers p with 2 <= p <= n, in increasing order.

# A prime number is a whole number greater than 1 whose only divisors are 1 and itself. If there are no primes in range, return an empty array.

# Example 1:
# Input: n = 10

# Output: [2,3,5,7]

# Example 2:
# Input: n = 1

# Output: []

# Constraints:
# 0 <= n <= 10^6.
# When n < 2, the answer is an empty array.





# Approach 1: Check Each Number

class Solution:
    def primesUpTo(self, n: int) -> list[int]:
        result = []
        # Test every candidate from 2 to n
        for m in range(2, n + 1):
            is_prime = True
            d = 2
            # A divisor above sqrt(m) pairs with one below, so stop at sqrt(m)
            while d * d <= m:
                if m % d == 0:
                    is_prime = False
                    break
                d += 1
            if is_prime:
                result.append(m)
        return result

# Complexity Analysis

# Time Complexity: O(n√n). For each of the n candidates, the divisor loop runs up to about √m steps, and m grows with n, so the total work scales with n times √n.
# Space Complexity: O(1) beyond the output. Only a flag and a few counters are kept, none of which grow with n. The result array itself holds the primes found.




# Approach 2: Sieve of Eratosthenes

class Solution:
    def primesUpTo(self, n: int) -> list[int]:
        if n<2:
            return []
        isPrime=[True]*(n+1)
        isPrime[0]=False
        isPrime[1]=False

        p=2
        while p*p<=n:
            if isPrime[p]:
                for i in range(p*p,n+1,p):
                    isPrime[i]=False
            p+=1
        return [i for i in range(2,n+1) if isPrime[i]]


# Complexity Analysis

# Time Complexity: O(n log log n). Each prime p crosses out about n / p multiples, and summing n / p over all primes up to n gives n times the sum of reciprocals of primes, which grows like log log n.
# Space Complexity: O(n). The boolean array holds one entry per number from 0 to n, so its size scales with n.




# 1. Correctness
# Your solution is correct. It uses the Sieve of Eratosthenes, which efficiently marks non-prime numbers and returns all primes from 2 to n in increasing order.
# It also correctly handles edge cases like n < 2 by returning [].

# 2. Time & Space Complexity
# Time: O(n log log n) — optimal for generating all primes up to n
# Space: O(n) — due to the boolean sieve array
# This is the standard best approach for this problem.

# 3. Code Quality
# The code is clean and easy to follow. Good use of:

# early return for small n
# sieve initialization
# starting elimination from p * p, which avoids redundant work
# Minor style improvements:

# Use is_prime instead of isPrime to follow Python naming conventions.
# Add a short comment explaining the sieve logic for readability.

# 4. Edge Cases
# You handled the important edge cases well:

# n = 0
# n = 1
# n = 2
# No functional issues are present.

# Overall
# This is a strong, efficient, and correct solution. The implementation is already at an excellent standard.

