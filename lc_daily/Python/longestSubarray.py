class Solution(object):
    def longestSubarray(self, nums):

        if nums.count(0) <= 1 or nums.count(1)==1:
            return nums.count(1) if nums.count(0) == 1 or nums.count(1)==1 else nums.count(1)-1

        nums = list(map(int, ''.join(map(str, nums)).strip('0')))
        indices = [index for index, value in enumerate(nums) if value == 0]

        if len(indices) == 0:
            return nums.count(1)

        l, r = 0, 0
        maxLen = 0
        for index in indices:
            if r > index:
                continue
            else:

                del nums[index]
                while r < len(nums) and nums[r] == 1:
                    r += 1
                maxLen = max(maxLen, len(nums[l:r]))
                nums.insert(index, 0)
                while nums[r] == 0:
                    r += 1
                l += 1

                while nums[l:r].count(0) > 0:
                    l += 1

        return maxLen

sln = Solution()
result = sln.longestSubarray([1, 1, 1])
print("Result: ", result)
