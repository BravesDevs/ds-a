class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1 and k == 1:
            return 0
        else:
            mid = pow(2, n-1)/2
            if (k <= mid):
                return self.kthGrammar(n-1, k)
            else:
                return int(not self.kthGrammar(n-1, k-mid))


sln = Solution()
print(sln.kthGrammar(2, 2))
