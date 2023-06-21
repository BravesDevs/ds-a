# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         minLength = len(nums)
#         if target in nums:
#             return 1
#         elif sum(nums)<target:
#             return 0
#         else:
#             l,r=0,1
#             while r<len(nums):
#                 summation = sum(nums[l:r+1])
#                 if summation<target:
#                     r+=1
#                 else:
#                     minLength=min(minLength,len(nums[l:r+1]))
#                     l+=1
#         return minLength

class Solution(object):
    def minSubArrayLen(self, target, nums):
        l,total=0,0
        res = float("inf")
        for r in range(len(nums)):
             total +=nums[r]

             while total>=target:
                res = min(res,r-l+1)
                total-=nums[l]
                l+=1
            

        
        return 0 if res == float("inf") else res

sln = Solution()
result = sln.minSubArrayLen(11,[1,2,3,4,5])
print("Result: ",result)