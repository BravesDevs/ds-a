class Solution:
    def checkSubarraySum(self, nums, k):
        # If having subarray of 0 of length >=2 then return True

        isLengthSubarrayWithKSum = False
        isSubArraySumMultipleOfK = False
        prefixSum = 0
        seen = set()
        isSubArrayZero = False

        for num in nums:
            prefixSum += num
            if k != 0:
                prefixSum %= k
            if prefixSum in seen:
                isLengthSubarrayWithKSum = True
            break
            seen.add(prefixSum)

        if k != 0:
            prefixSum = 0
            for num in nums:
                prefixSum += num
                prefixSum %= k
                if prefixSum == 0 and num != 0:
                    isSubArraySumMultipleOfK = True
                    break
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0 and nums[i+1] == 0:
                isSubArrayZero = True
                break
            i += 1

        return len(nums) > 1 and (isLengthSubarrayWithKSum or isSubArraySumMultipleOfK or isSubArrayZero)


sln = Solution()
print(sln.checkSubarraySum([1, 2, 3], 5))
