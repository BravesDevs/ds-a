class Solution:
    def lemonadeChange(self, bills):
        changeMap = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                changeMap[5] += 1 
            elif bill == 10:
                if changeMap[5] > 0:  
                    changeMap[5] -= 1
                    changeMap[10] += 1 
                else:
                    return False 
            elif bill == 20:
                if changeMap[10] > 0 and changeMap[5] > 0:
                    changeMap[10] -= 1
                    changeMap[5] -= 1
                elif changeMap[5] >= 3:  
                    changeMap[5] -= 3
                else:
                    return False  
            else:
                return False  
        return True  


sln = Solution()
print(sln.lemonadeChange([5, 5, 10, 20, 5, 5, 5,
      5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
