# Count Frequency of Each Element

# Given an integer array nums, return a 2D array where each row is [value, count], giving the frequency of every distinct value in nums.

# The rows must be ordered by the value's first appearance in nums. If the array is empty, return an empty array.

# Example 1:
# Input: nums = [1, 2, 2, 3]

# Output: [[1,1],[2,2],[3,1]]

# Example 2:
# Input: nums = [-1, -1, 2, -1, 2]

# Output: [[-1,3],[2,2]]

# Constraints:
# 0 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# The order of rows follows the first appearance of each value in nums.

# Approach 1: Hash Map
class Solution:
    def count_frequency(self, nums: List[int]) -> List[List[int]]:
        w={}
        for i in nums:
            w[i]=w.get(i,0)+1
        return [[num, count] for num, count in w.items()]


# Time & Space Complexity
# Time: O(n) — one pass through the array
# Space: O(n) — hash map to store the frequency of each distinct value