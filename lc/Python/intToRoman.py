class Solution:

    
    def intToRoman(self, num):
        intRomanDict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
        }

        nums = list(intRomanDict.keys())
        index=0
        romanStr = ''
        while num > 0:
            charCount = num // nums[index]
            romanStr += charCount*intRomanDict[nums[index]]
            num-= charCount*nums[index]
            index+=1
        
        return romanStr



sln = Solution()
result = sln.intToRoman(1994)
print("Result: ",result)