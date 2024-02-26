class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        slow = 0
        fast = 0
        count = 0
        while fast < len(nums):
            if nums[fast] == 1:
                count = max(count, (fast-slow)+1)
                fast += 1
            else:
                fast = fast+1
                slow = fast
        return count


sln = Solution()
print(sln.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
