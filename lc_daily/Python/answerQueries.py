class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        res = []
        for i in queries:

            l = 0
            r = len(nums)-1

            while l <= r:
                mid = (l+r)//2

                if nums[mid] <= i:
                    l = mid+1
                else:
                    break
            res.append(mid)
        return res


sln = Solution()

print(sln.answerQueries([4, 5, 2, 1], [3, 10, 21]))
