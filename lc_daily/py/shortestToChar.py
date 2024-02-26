class Solution:
    def shortestToChar(self, s, c):
        left, right, output = [None]*len(s), [None]*len(s), [None]*len(s)
        tmp = float('inf')
        for i in range(len(s)):
            if s[i] == c:
                tmp = 0
            left[i] = tmp
            tmp += 1

        tmp = float("inf")
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                tmp = 0
            right[i] = tmp
            tmp += 1

        for i in range(len(s)):
            output[i] = min(left[i], right[i])
        return output


sln = Solution()
print(sln.shortestToChar("leet", 'e'))
