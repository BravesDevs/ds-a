class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start = nums[0]
        end = nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
        return result


sln = Solution()
result = sln.summaryRanges([0, 1, 2, 4, 5, 7])

print("Result: ", result)
