from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers,  return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.
    """
    value_index_cache = {}

    for i, num in enumerate(nums):
        search_value = target - num
        if search_value in value_index_cache:
            return [value_index_cache[search_value], i]
        else:
            # Assume 1 solution so overwriting is not a concern
            value_index_cache[num] = i
    return []
