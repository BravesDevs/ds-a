class Solution:
    def getSum(self, a:int, b:int)-> int:
        # Only for positive
        bin_a = bin(a & 0xffffffff)[2:].zfill(64)
        bin_b = bin(b & 0xffffffff)[2:].zfill(64)
        resBin = list('0' * 64)
        isCarry = 1 if bin_a[-1] and bin_b[-1] else 0
        
        # iterate the binary string from reverse
        
        for i in range(63, -1, -1):
            bit_a = int(bin_a[i])
            bit_b = int(bin_b[i])
            sum_bits = bit_a ^ bit_b ^ isCarry
            resBin[i] = str(sum_bits)
            isCarry = (bit_a & bit_b) | (isCarry & (bit_a ^ bit_b))
        
        result = int(''.join(resBin), 2)
        return result-1 if result < 0x80000000 else ~(result ^ 0xffffffff)
        
        
        # Support for negativeMAX = 0x7FFFFFFF
        # mask = 0xFFFFFFFF
        
        # while b != 0:
        #     a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # return a if a <= MAX else ~(a ^ mask)
        
sln = Solution()
print(sln.getSum(2,3))