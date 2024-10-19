class Solution:
    def findKthBit(self, n, k):
        # S1=0
        # Si=Si-1 + "1" + reverse(invert(Si-1))

        def invert(s):
            return "".join(["1" if c == "0" else "0" for c in s])

        def reverse(s):
            return s[::-1]

        def helper(n, k):
            if n == 1:
                return "0"
            mid = 2 ** (n - 1)
            if k == mid:
                return "1"
            elif k < mid:
                return helper(n - 1, k)
            else:
                return invert(reverse(helper(n - 1, 2 ** n - k)))

        return helper(n, k)


sln = Solution()
print(sln.findKthBit(3, 1))  # 0
print(sln.findKthBit(4, 11))  # 1
