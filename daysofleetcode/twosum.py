import enum
from typing import List


class Solution:
    def calculator_two_sum(self, nums: List[int], target: int) -> list[int]:
        map = {}
        for idx , value in enumerate(nums):
            diff = target - value
            if diff in map:
                print(map[diff], idx)
                return [map[diff], value]
            map[value] =  idx


Solution.calculator_two_sum(Solution, [2,10,5,7,13], target=9)