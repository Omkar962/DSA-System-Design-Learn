# Second Largest Element

# Given an integer array nums, return the second largest distinct value in the array.

# If the array does not contain a second distinct value, return -1. For example, [5, 5, 4] returns 4, while [5, 5, 5] returns -1 because every element is the same.

# Example 1:
# Input: nums = [3, 9, 5]

# Output: 5

# Example 2:
# Input: nums = [5, 5, 5]

# Output: -1

# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# The second largest refers to the second largest distinct value. Duplicates of the maximum do not count.


# Approach 1: One Pass

class Solution:
    def second_largest(self, nums: List[int]) -> int:
        largest=float("-inf")
        second=float("-inf")
        for x in nums:
            if x>largest:
                second=largest
                largest=x
            elif x<largest and x>second:
                second=x
        return -1 if second==float("-inf") else second


# Time & Space Complexity
# Time: O(n) — one pass through the array
# Space: O(1) — only two variables are used