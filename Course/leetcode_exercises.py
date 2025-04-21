# Trying exercises from leetcode 
# Two Sum

# Instead of using two nested loops (O(n^2) time),
# we use a hash map (dictionary in Python) to store numbers we've seen.
# For each number, we calculate its complement (target - number).
# If the complement is already in the map, we return the pair of indices.
# This reduces the time complexity to O(n).

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}                    # map with number from nums and index
        for i, num in enumerate(nums):  # enumerate is similar to loop in c++
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

