class Solution:
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters)-1

        result = letters[0]
        while l <= r:
            mid = (l+r)//2
            if letters[mid] > target:
                result = letters[mid]
                r = mid-1
            else:
                l = mid+1
            mid = (l+r)//2

        return result


sln = Solution()
print(sln.nextGreatestLetter(["c", "f", "j"], "c"))
