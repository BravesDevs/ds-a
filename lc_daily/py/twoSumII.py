class Solution:
    def twoSum(self, numbers, target):
        for index,element in enumerate(numbers):
            if(target-element in numbers[index+1:]):
                numbers[index]=-999
                return [index+1, numbers.index(target-element)+1]

    
sln = Solution()
result = sln.twoSum([-1,0],-1)
print("Result: ",result)