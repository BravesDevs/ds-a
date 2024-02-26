class Solution:

    def compress(self, chars):
        index = 0
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            num = j - i
            chars[index] = chars[i]
            index += 1
            if num > 1:
                for digit in str(num):
                    chars[index] = digit
                    index += 1
            i = j
        return index


sln = Solution()
print(sln.compress(["a", "a", "b", "b", "c", "c", "c"]))
