class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr, ans = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                ans.append(curr[:])
                return

            if curr_sum > target or i == len(candidates):
                return

            backtrack(i + 1, curr_sum)

            curr.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            curr.pop()

        backtrack(0, 0)
        return ans

        