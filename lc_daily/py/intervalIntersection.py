class Solution:
    def intervalIntersection(self, A, B):
        res = []

        p1 = 0
        p2 = 0

        while p1 < len(A) and p2 < len(B):
            # Checking if the points are intersecting
            if  B[p2][0]<=A[p1][1] and A[p1][0]<=B[p2][1]:
                res.append([max(A[p1][0],B[p2][0]),min(A[p1][1],B[p2][1])])
            
            if A[p1][1]>B[p2][1]:
                p2+=1
            else:
                p1+=1

        return res

sln = Solution()
print(sln.intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
