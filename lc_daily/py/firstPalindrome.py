class Sol:
    def firstPalindrome(self, words):
        for i in words:
            l = 0
            r = len(i)-1

            if len(i) % 2 == 0:
                while l < r:
                    if i[l] != i[r]:
                        break
                    l += 1
                    r -= 1
                if l >= r:
                    return i
            else:
                while l <= r:
                    if i[l] != i[r]:
                        break
                    l += 1
                    r -= 1
                if l > r:
                    return i


sln = Sol()
print(sln.firstPalindrome(["pp"]))
