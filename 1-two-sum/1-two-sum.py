class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for f_idx in range(len(nums)):
            for t_idx in range(f_idx+1, len(nums)):
                if nums[f_idx]+nums[t_idx]==target:
                    return [f_idx,t_idx]