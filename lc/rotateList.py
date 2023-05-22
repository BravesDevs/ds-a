class Solution:
    def rotate(self, nums, k):
        if k == 0 or k % len(nums)==0:
            return nums
        else:
            tempList = nums[len(nums)-k:]
            del nums[len(nums)-k:]
            for i in tempList[::-1]:
                nums.insert(0,i)
        print(nums)

sln = Solution()
answer = sln.rotate([1,2],5)
print(answer)