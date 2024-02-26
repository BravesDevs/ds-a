class Sol:

    def rev(self, num):
        return int(str(num)[::-1])

    def countNicePairs(self, nums):
        mod = 1000000007

        freq = {}
        ans = 0
        for i in nums:
            val = i-self.rev(i)
            if not freq.get(val):
                freq[val] = 0
            ans += freq[val] % mod
            freq[val] += 1
        return ans % mod


sln = Sol()
print(sln.countNicePairs([13, 10, 35, 24, 76]))
