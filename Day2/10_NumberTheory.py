# gcd(a, b) * lcm(a, b) = a * b

#GCD of Two Numbers

# Given two non-negative integers a and b, return their greatest common divisor, the largest positive integer that divides both a and b with no remainder.

# Follow the standard conventions for zero: gcd(a, 0) = a, gcd(0, b) = b, and gcd(0, 0) = 0. The inputs are non-negative. For negative inputs you would take the absolute values first, since the divisors of a number are the same as the divisors of its negation.

# Example 1:
# Input: a = 12, b = 18

# Output: 6

# Example 2:
# Input: a = 17, b = 5

# Output: 1

# Constraints:
# 0 <= a, b <= 2^31 - 1
# a and b are non-negative.
#At least one of a or b may be 0.

import math
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a,b=b,a%b
        return a


# Complexity Analysis

# Time Complexity: O(log(min(a, b))). Each remainder step at least halves the smaller value within two iterations, so the number of steps grows with the logarithm of the input.
# Space Complexity: O(1). The algorithm updates two values in place with no extra storage.


# LCM of Two Numbers


# Given two positive integers a and b, return their least common multiple: the smallest positive integer that is divisible by both a and b.

# By convention, if either number is 0, the least common multiple is 0. The test cases use positive inputs.

# Example 1:
# Input: a = 4, b = 6

# Output: 12

# Example 2:
# Input: a = 3, b = 5

# Output: 15

# Constraints:
# 1 <= a, b <= 10^4
# a and b are positive integers


class Solution:
    def lcm(self, a: int, b: int) -> int:
        x,y=a,b
        while y:
            x,y=y,x%y
        
        return (a//x)*b

# Complexity Analysis

# Time Complexity: O(log(min(a, b))). The Euclidean algorithm reduces the pair in a number of steps proportional to the logarithm of the smaller value. The division and multiplication that follow are constant-time.
# Space Complexity: O(1). Only a few scalar variables are used, independent of the input size.



# Perfect Number Check

# Given an integer n, return true if n is a perfect number and false otherwise.

# A perfect number is a positive integer that equals the sum of its proper divisors. The proper divisors of a number are its positive divisors excluding the number itself. For example, 6 has proper divisors 1, 2, and 3, and 1 + 2 + 3 = 6, so 6 is perfect. Any value of n that is 1 or smaller, including 0 and negative numbers, is not perfect.

# Example 1:
# Input: n = 6

# Output: true

# Example 2:
# Input: n = 12

# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1
# n may be negative, zero, or positive.

# Approach 1: Sum Divisors up to n-1  

class Solution:
    def isPerfect(self, n: int) -> bool:
        # A perfect number must be a positive integer greater than 1
        if n <= 1:
            return False
        total = 0
        # Add every proper divisor below n
        for i in range(1, n):
            if n % i == 0:
                total += i
        return total == n

# Complexity Analysis

# Time Complexity: O(n). The loop tests every integer from 1 up to n - 1, so the number of iterations grows linearly with n.
# Space Complexity: O(1). The running sum is the only extra storage, and its size does not depend on n.



#Approach 2: Square-Root Divisor Pairs

class Solution:
    def isPerfect(self, n: int) -> bool:
        if n<2:
            return False
        i=2
        total=1
        while i*i<=n:
            if n%i==0:
                total+=i
                pair=n//i
                if pair!=i:
                    total+=pair
            i+=1
        return total==n

# Complexity Analysis

# Time Complexity: O(sqrt n). The loop runs only while i * i stays at most n, so it stops near the square root instead of scanning every value below n.
# Space Complexity: O(1). The running sum and the paired divisor are the only extra storage, and neither grows with n.


# Decimal to Binary

# Given a non-negative integer n, return its binary representation as a string of 0s and 1s.

# The result must not contain leading zeros, with one exception: the value 0 returns the single-character string "0".

# Example 1:
# Input: n = 10

# Output: "1010"

# Example 2:
# Input: n = 0

# Output: "0"

# Constraints:
# 0 <= n <= 2^31 - 1
# n is a non-negative integer.

class Solution:
    def decimalToBinary(self, n: int) -> str:
        if n==0:
            return"0"
        bits=[]

        while n:
            bits.append(str(n%2))
            n=n//2
        return "".join(reversed(bits))


# Complexity Analysis

# Time Complexity: O(b), where b is the number of bits in n. Since the bit count grows with the logarithm of the value, this is O(log n). The loop runs once per bit, and the reversal touches each bit once more.
# Space Complexity: O(b). The buffer holds one character per bit, so its size grows with the number of bits.