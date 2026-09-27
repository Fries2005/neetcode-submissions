class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in targets:
                return[targets[target-num], i]

            targets[num] = i

        return []