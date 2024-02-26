class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False


sln = Solution()
print(sln.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
