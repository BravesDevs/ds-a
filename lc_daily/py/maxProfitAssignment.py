class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        i, max_profit, res = 0, 0, 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            res += max_profit
        return res
