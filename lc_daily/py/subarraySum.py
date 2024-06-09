class Solution:
    def subarraysDivByK(self, nums, k):
        prefixSum = 0
        seen = {0: 1}
        count = 0
        for num in nums:
            prefixSum += num
            mod = prefixSum % k
            count += seen.get(mod, 0)
            seen[mod] = seen.get(mod, 0) + 1
        return count



sln = Solution()
print(sln.subarraySum([1, 2, 3], 3))