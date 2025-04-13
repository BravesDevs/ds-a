class Solution:
    def fourSum(self, nums,target):
        res = []
        nums.sort()
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1,N):
                l, r = j+1, len(nums)-1
                while l < r:
                    summ = nums[i]+nums[j]+nums[l]+nums[r]
                    if summ == target and [nums[i],nums[j],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while l<N and nums[l]==nums[l-1]:
                            l+=1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
        return res
    
sln = Solution()
print(sln.fourSum([-3,-1,0,2,4,5],2))