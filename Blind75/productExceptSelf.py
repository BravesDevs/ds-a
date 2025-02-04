import math
class Solution:
    def productExceptSelf(self,nums):
        prefix = [1]
        postfix = [1]
        
        for i in range(0,len(nums)):
            prefix.append(prefix[i]*nums[i])
            postfix.append(postfix[i]*nums[len(nums)-1-i])
        
        prefix.pop(0)
        postfix.pop(0)
        postfix.reverse()        
    
        result = [postfix[1]]
        
        for i in range(1,len(nums)-1):
            result.append(prefix[i-1]*postfix[i+1])
            
        result.append(prefix[len(nums)-2])
        
        return result
        
        
sol = Solution()
# Test 1
print(sol.productExceptSelf([-1,1,0,-3,3]))