class Solution:
    def findComplement(self, num):
        binary = bin(num)[2:]
        return int(''.join('1' if bit == '0' else '0' for bit in binary), 2)


sln = Solution()
print(sln.findComplement(5))
