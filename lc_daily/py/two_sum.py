class Solution:
    # ! Not Optimised Solution
    # def twoSum(self, nums, target):
    #     i = 0
    #     while i < len(nums):
    #         j = i+1
    #         while j < len(nums):
    #             if nums[j]+nums[i] == target:
    #                 return [i, j]
    #             else:
    #                 j += 1
    #         i += 1

    def twoSum(self, nums, target):
        hashMap = {}

        for index, element in enumerate(nums):
            if hashMap.get(target-element) is None:
                hashMap[element] = index
            else:
                return [hashMap[target-element], index]


sln = Solution()
result = sln.twoSum([2, 7, 11, 15], 9)
print("Result: ", result)
