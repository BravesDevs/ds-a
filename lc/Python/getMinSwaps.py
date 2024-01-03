import copy


class Sol:
    def getMinSwaps(self, num, k):
        def nextPermutation():
            def reverse(l, r):
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            index1 = -1
            for i in range(n-2, -1, -1):
                if nums[i] < nums[i+1]:
                    index1 = i
                    break

            if index1 != -1:
                index2 = -1
                for i in range(n-1, 0, -1):
                    if nums[i] > nums[index1]:
                        index2 = i
                        break
            nums[index1], nums[index2] = nums[index2], nums[index1]
            reverse(index1+1, n-1)
        nums = list(num)
        n = len(nums)
        oldNums = nums.copy()
        while k:
            nextPermutation()
            k -= 1
        ans = 0

        for i in range(n):
            if nums[i] != oldNums[i]:
                j = i+1

            while oldNums[j] != nums[i]:
                j += 1

            while j != i:
                oldNums[j], oldNums[j-1] = oldNums[j-1], oldNums[j]
                j -= 1
                ans += 1
        return ans


sln = Sol()
print(sln.getMinSwaps("11112", 4))
