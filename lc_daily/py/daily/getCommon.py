class Solution:
    def getCommon(self, nums1, nums2):
        i, j = 0, 0
        result = -1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result


sln = Solution()

print(sln.getCommon([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
