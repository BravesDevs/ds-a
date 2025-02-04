class Solution:
    def maxSubArray(self,nums):
        #* Brute Force O(n^2)
        # res = nums[0]
        
        # for i in range(0,len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         res = max(res,sum)     
        # return res
        
        #* Kadane's Algorithm O(n)
        maxSum = nums[0]
        currentSum = nums[0]
        
        for i in range(1,len(nums)):
            # If the current sum is less than the current number, then the current sum is the current number 
            currentSum = max(nums[i],currentSum+nums[i])
            maxSum = max(maxSum,currentSum)
            
        return maxSum
        
        pass
    
    
sol = Solution()
print(sol.maxSubArray([-1])) # 1