class Solution:
    def sumOddLengthSubarrays(self, arr):
        N = len(arr)
        total = 0

        for i in range(1, N+1, 2):
            for k in range(N-i+1):
                total += sum(arr[k:i+k])
        return total


sln = Solution()

print(sln.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
