class Solution:
    def findArray(self, nums):
        p1 = -1
        p2 = 0
        res = []
        while p2 < len(nums):
            if p1 < 0:
                res.append(nums[p2])
            else:
                # Compute XOR of nums[p1] and nums[p2]
                res.append(nums[p1] ^ nums[p2])
            p1 = p2
            p2 += 1
        return res


sln = Solution()

print(sln.findArray([13]))
