class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list(itertools.combinations(range(1, n+1), k))
        return ans