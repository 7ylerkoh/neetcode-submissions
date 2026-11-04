class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            complement = target - num
            # if complement in complements:
            #     return [complements[complement], i]
            # complements[num] = i

            # complements[i] = complement

            if num in complements:
                return [complements[num], i]
            complements[complement] = i
        