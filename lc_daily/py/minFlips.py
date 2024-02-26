
class Solution:
    def minFlips(self, a, b, c):

        if (a == b and b == c) or (a+b == c):
            return 0
        
        maxNum = len(bin(max([a,b,c])).replace("0b",""))
        print("Max:",maxNum)

        binaryA = format(a, f"0{maxNum}b")
        binaryB = format(b, f"0{maxNum}b")
        binaryC = format(c, f"0{maxNum}b")

        flips=0
        for i in range(len(binaryA)):
            if binaryC[i] == '0':
                if binaryA[i]=='1':
                    flips+=1
                if binaryB[i]=='1':
                    flips+=1
            else:
                if binaryA[i] == '1' or binaryB[i]=='1':
                    continue
                else:
                    flips+=1
        return flips


sln = Solution()
result = sln.minFlips(2, 6, 5)
print("Result: ", result)
