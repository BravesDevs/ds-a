class Solution:
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1 = nums2
        elif n == 0:
            nums1 = nums1
        else:
            
    def push_and_shift(self, arr, element, index):
        arr.append(None)  
        for i in range(len(arr)-1, index, -1):
            arr[i] = arr[i-1]        
        arr[index] = element


sln = Solution()
sln.merge([1,2,3,0,0,0],3,[2,5,6],3)