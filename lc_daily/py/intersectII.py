class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        countDict = {}

        for i in nums1:
            countDict[i] = nums1.count(i)

        result = []
        for i in nums2:
            count = countDict.get(i)
            if count is not None and count > 0:
                result.append(i)
                countDict[i] = countDict[i]-1

        return result


sln = Solution()
print(sln.intersect([1, 2, 2, 1], [2, 2]))
