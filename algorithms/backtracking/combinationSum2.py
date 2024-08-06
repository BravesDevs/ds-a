class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        # Backtrack
        candidates.sort()

        def backtrack(cur, pos, target):
            if not target:
                result.append(cur.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidate == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target-candidates[i])
                cur.pop()
                prev = candidate
        backtrack([], 0, target)
        return result
