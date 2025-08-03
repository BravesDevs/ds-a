from collections import defaultdict

class Solution:
    def threeSum(self,nums):
        nums.sort()
        res = []
        N = len(nums)
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r=i+1,N-1

            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                arr = [nums[i],nums[l],nums[r]]

                if summ==0:
                    res.append(arr)
                    l+=1
                    while l<N and nums[l]==nums[l-1]:
                        l+=1
                elif summ<0:
                    l+=1
                else:
                    r-=1
        return res


    
sln = Solution()
print(sln.threeSum([-1,0,1,2,-1,-4]))
