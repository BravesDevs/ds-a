class Solution(object):
    def getAverages(self, nums, k):
        dictMap = {
        }
        if len(nums)<k:
            return [-1]*len(nums)
        elif k==0:
            return nums
        else:
            res=[]
            for i in range(len(nums)):
                prev_pointer = i - k
                next_pointer = i + k
                if prev_pointer>=0 and next_pointer<len(nums):
                    summation = sum(nums[prev_pointer:next_pointer+1])
                    if not summation in dictMap:
                        result = summation//((k*2)+1)
                        dictMap[summation] = result
                        res.append(result)
                    else:
                        res.append(dictMap[summation])
                    
                else:
                    res.append(-1)
            return res

sln = Solution()
result = sln.getAverages([7,4,3,9,1,8,5,2,6],3)
print("Result: ",result)