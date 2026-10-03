# Reverse an Array In Place

# Given an integer array nums, reverse the order of its elements in place and return the reversed array.

# Reversing in place means you must rearrange the elements within the same array. Do not allocate a second array to hold the result.

# Example 1:
# Input: nums = [1, 2, 3, 4]

# Output: [4, 3, 2, 1]

# Example 2:
# Input: nums = [-3, -1, -2, -5, -4]

# Output: [-4, -5, -2, -1, -3]

# Constraints:
# 0 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# You must modify the array in place using O(1) extra space.

# Approach 1: Two Pointers

class Solution:
    def reverse_array(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums

# Time & Space Complexity
# Time: O(n) — one pass through the array
# Space: O(1) — only two variables are used