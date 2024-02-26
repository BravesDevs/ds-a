# import copy
# class Solution:
#     def threeSum(self,nums):
#         nums.sort()
#         result = []
#         i=0
#         while i<=len(nums)-1 and nums[i]<=0:

#             if i>0 and nums[i]==nums[i-1]:
#                 i+=1
#                 continue

#             dupli = copy.deepcopy(nums)
#             dupli[i]=-9999
#             for j in range(i+1,len(nums)):
#                 dupli[j]=-9999
#                 summation = nums[i]+nums[j]
#                 if summation>0:
#                     break
#                 if((summation*-1) in dupli):
#                     res=sorted([nums[i],nums[j],nums[dupli.index(summation*-1)]])
#                     if res not in result:
#                         result.append(res)
#             i+=1
#         return result

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for index, element in enumerate(nums):
            if index > 0 and element == nums[index-1]:
                continue

            l, r = index+1, len(nums)-1

            while l < r:
                summ = element+nums[l]+nums[r]

                if summ == 0:
                    res.append([element, nums[l], nums[r]])
                    l += 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return res


sln = Solution()

result = sln.threeSum([0, 0, 0])
print(result)
