class Solution:
    def findErrorNums(self, nums):
        length = len(nums)

        occurance = {i: 0 for i in range(1, length+1)}

        for i in nums:
            occurance[i] += 1

        value = [i for i in occurance if occurance[i] == 2]
        missing = [i for i in occurance if occurance[i] == 0]

        value.extend(missing)
        return value


sln = Solution()
print(sln.findErrorNums([1, 2, 2, 4]))
