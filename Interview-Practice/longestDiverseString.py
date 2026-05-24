class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        whichCharMax = 'a' if a >= b and a >= c else 'b' if b >= a and b >= c else 'c'
        # If whichCharMax is more than 2 times the sum of the other two, we can only use 2 of it and then we have to use the other two characters to avoid having 3 in a row.
        whichNext = []
        if whichCharMax == 'a' and a > 2 * (b + c):
            res.append('a')
            res.append('a')
            a -= 2
            whichNext = [b,c]
        elif whichCharMax == 'b' and b > 2 * (a + c):
            res.append('b')
            res.append('b')
            b -= 2
            whichNext = [a,c]
        elif whichCharMax == 'c' and c > 2 * (a + b):
            res.append('c')
            res.append('c')
            c -= 2
            whichNext = [a,b]

        while a > 0 or b > 0 or c > 0:
            # Check from whichNext we can use a character, if both are 0, we can use the whichCharMax character, otherwise we have to use the one that is not 0 to avoid having 3 in a row.
            if whichNext:
                if whichNext[0] > 0:
                    if whichNext[1] > 0:
                        if whichNext[0] >= whichNext[1]:
                            res.append('b' if whichCharMax == 'a' else 'a')
                            whichNext[0] -= 1
                        else:
                            res.append('c' if whichCharMax == 'a' else 'b')
                            whichNext[1] -= 1
                    else:
                        res.append('b' if whichCharMax == 'a' else 'a')
                        whichNext[0] -= 1
                elif whichNext[1] > 0:
                    res.append('c' if whichCharMax == 'a' else 'b')
                    whichNext[1] -= 1
                else:
                    # both are 0, we can use the whichCharMax character
                    if whichCharMax == 'a':
                        res.append('a')
                        a -= 1
                    elif whichCharMax == 'b':
                        res.append('b')
                        b -= 1
                    elif whichCharMax == 'c':
                        res.append('c')
                        c -= 1
            else:
                if whichCharMax == 'a':
                    res.append('a')
                    a -= 1
                elif whichCharMax == 'b':
                    res.append('b')
                    b -= 1
                elif whichCharMax == 'c':
                    res.append('c')
                    c -= 1
            return ''.join(res)

sln = Solution()
print(sln.longestDiverseString(1,1,7))