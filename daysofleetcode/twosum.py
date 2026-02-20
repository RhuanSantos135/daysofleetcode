from typing import List



class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:

        map = {}

        for idx, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return [map[diff], idx]
            map[value] = idx

Solution.twoSum(nums=[7,11,15,2], target= 9)