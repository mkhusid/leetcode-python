class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {n: i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            res = nums_dict.get(target - n)
            if (res is not None) & (i != res):
                return i, res