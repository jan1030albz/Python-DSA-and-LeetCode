"""Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order."""

from operator import index
from typing import List

# Example Inputs
# nums = [2,7,11,15], target = 9
# answer = [1,2]

# nums = [3,2,4], target = 6
# answer = [1,2]

# nums = [3,3], target = 6
# answer = [0,1]


# BRUTEFORCE
def bf_two_sum(nums: List[int], target: int) -> List[int]:
    """Takes alot of time for very large inputs:
    O(n^2)
    O(1)
    """
    for index, first in enumerate(nums):
        for index_2, second in enumerate(nums):
            if index == index_2:
                continue
            if first + second == target:
                return [index, index_2]
    return None


# No Repeats
def nr_two_sum(nums: List[int], target: int) -> List[int]:
    """Takes alot of time for very large inputs:
    O(n^2)
    O(1)
    """
    index_to_right = 1
    for index, first in enumerate(nums):
        for index_2, second in enumerate(nums[index_to_right:]):
            if first + second == target:
                return [index, index_2 + index_to_right]
        index_to_right += 1
    return None


# https://www.code-recipe.com/post/two-sum
# Using HashMap
def hm_two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            return [i, seen[remaining]]
        seen[value] = i


def bs_two_sum(nums: List[int], target: int) -> List[int]:
    """Takes alot of time for very large inputs:
    O(nb)
    O(1)
    """
    map_iterated = {}
    for index_, number in enumerate(nums):
        if number < target:
            map_iterated[index_] = number
     
