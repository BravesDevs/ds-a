from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)

        max_count = max(count.values())
        max_count_tasks = sum(
            1 for task, count in count.items() if count == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


sln = Solution()
print(sln.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
