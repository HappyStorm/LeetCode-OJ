class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, _len = [], len(candidates)
        candidates.sort()

        def find_ans(res, index, goal):
            if goal == 0:
                ans.append(res)
                return
            else:
                while index < _len and candidates[index] <= goal:
                    _member = candidates[index]
                    find_ans(res+[_member], index, goal-candidates[index])
                    index += 1
                return
        find_ans([], 0, target)
        return ans
