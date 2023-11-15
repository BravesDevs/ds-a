class Solution:
    def findMaxAverage(self, nums, k):
        if k > len(nums):
            return None

        summation = sum(nums[0:k])
        avg = summation/float(k)
        for i in range(k, len(nums)):
            newSummation = summation+(nums[i]-nums[i-k])
            if summation != newSummation:
                summation = newSummation
                avg = max(avg, summation/float(k))

        return avg


sln = Solution()
print(sln.findMaxAverage([5], 1))
