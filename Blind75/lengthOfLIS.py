class Solution:
    def lengthOfLIS(self,nums):
        array = [nums[0]]
        for i in range(len(nums)):
            if nums[i]>array[-1]:
                array.append(nums[i])
            else:
                l,r=0,(len(array)-1)
                
                mid = (l+r)//2
                array[mid]=nums[i]
        return len(array)
        