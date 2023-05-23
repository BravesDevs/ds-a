class Solution:
    def canJump(self, nums):
        goalPost = len(nums)-1
        print(goalPost)
        i=goalPost
        while goalPost>0 and i > 0:
            if goalPost + nums[i] >= goalPost:
                goalPost=i
            i-=1
        return True

        

        
sln = Solution()
result = sln.canJump([3,2,1,0,4])
print("Result: ",result)
