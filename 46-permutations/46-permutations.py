class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list(itertools.permutations(nums))
        return ans