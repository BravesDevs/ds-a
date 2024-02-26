from collections import deque


class Solution:
    def reformat(self, s):
        if len(s) == 1:
            return s

        chars = deque(x for x in s if x.isalpha())
        nums = deque(x for x in s if x.isdigit())

        if abs(len(chars) - len(nums)) > 1:
            return ""

        res = []
        if len(nums) > len(chars):
            while nums:
                res.append(nums.popleft())
                if chars:
                    res.append(chars.popleft())
        else:
            while chars:
                res.append(chars.popleft())
                if nums:
                    res.append(nums.popleft())

        return ''.join(res)


sln = Solution()
print(sln.reformat("ab123"))
