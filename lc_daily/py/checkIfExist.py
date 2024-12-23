class Solution: 
    def checkIfExist(self,arr):
        arr.sort()
        l=0
        while l<len(arr)-1:
            for r in range(l+1,len(arr)):
                # Handle for negative values
                if arr[l]<0 and arr[r]<0:
                    if arr[r]==arr[l]/2:
                        return True
                    if arr[r]>arr[l]/2:
                        break
                if arr[r]==arr[l]*2:
                    return True
                if arr[r]>arr[l]*2:
                    break
            l+=1


        return False

sln = Solution()
print(sln.checkIfExist([-10,12,-20,-8,15]))