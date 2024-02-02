class Solution:
    def sequentialDigits(self, low, high):
        nums = [str(x) for x in range(1, 10)]
        lowlen = len(str(low))
        highlen = len(str(high))
        res = []
        for elements in range(lowlen, highlen+1):
            for i in range(0, (len(nums)-elements)+1):
                num = int(''.join(nums[i:i+elements]))

                if low <= num and num <= high:
                    res.append(num)
        return res


sln = Solution()
print(sln.sequentialDigits(1000, 13000))
