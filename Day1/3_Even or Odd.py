# Even or Odd

# Given an integer n, determine whether it is even or odd.

# Return the string "Even" if n is divisible by 2, and "Odd" otherwise.

# Example 1:
# Input: n = 4

# Output: "Even"

# Example 2:
# Input: n = -3

# Output: "Odd"

# Constraints:
# n is an integer that fits in a 32-bit signed range.
# n can be negative, zero, or positive.


# Approach 1 = Modulo Check

class Solution:
    def evenOrOdd(self, n: int) -> str:
        # Compare the remainder against 0 so negatives are handled correctly
        if n % 2 != 0:
            return "Odd"
        return "Even"

# Complexity Analysis

# Time Complexity: O(1). A single division and comparison run in constant time regardless of the value of n.
# Space Complexity: O(1). No extra storage is used beyond the returned string.


# Approach 2 = Bitwise AND

class Solution:
    def evenOrOdd(self, n: int) -> str:
        # The lowest bit is 1 for odd numbers and 0 for even numbers
        if n & 1:
            return "Odd"
        return "Even"


# Complexity Analysis

# Time Complexity: O(1). Extracting one bit and comparing it is a constant-time operation.
# Space Complexity: O(1). The result string is the only allocation, and its size does not depend on n.




# Leap Year
class Solution:
    def isLeapYear(self, year: int) -> bool:
        # Divisible by 4, and either not a century year or divisible by 400
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



# Sum of Even or Odd Numbers from 1 to N
class Solution:
    def sum_by_parity(self, n: int, parity: str) -> int:
        odd=0
        even=0
        for i in range(n+1):
            if i%2==0:
                even+=i
            else:
                odd+=i
        return odd if parity=="odd" else even

# Complexity Analysis

# Time Complexity: O(n). The loop runs once for every integer from 1 to n.
# Space Complexity: O(1). Only the target remainder and the running total are stored, regardless of n.