class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, n in enumerate(nums):
            indexes[n] = i

        for i, n in enumerate(nums):
            complement = target - n

            if complement in indexes and indexes[complement] != i:
                return [i, indexes[complement]]

        return []
        