class Sol:
    def leftRightDifference(self, nums):
        leftSum = 0
        rightSum = sum(nums[1:])
        res = [abs(rightSum-leftSum)]

        for i in range(1, len(nums)):
            rightSum -= nums[i]
            leftSum += nums[i-1]

            res.append(abs(rightSum-leftSum))

        return res


sln = Sol()

print(sln.leftRightDifference([1]))
