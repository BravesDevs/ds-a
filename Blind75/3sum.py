from collections import Counter
class Solution:
    def threeSum(self,nums):
        res = []
        nums.sort()
        N = len(nums)
        for index, element in enumerate(nums):
            if index > 0 and element == nums[index-1]:
                continue

            l, r = index+1, len(nums)-1

            while l < r:
                summ = element+nums[l]+nums[r]

                if summ == 0:
                    res.append([element, nums[l], nums[r]])
                    l+=1
                    while l<N and nums[l]==nums[l-1]:
                        l+=1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return res
        
        
sln = Solution()
print(sln.threeSum([0,0,0,0]))