class Solution:
    def decodeMessage(self, key, s):

        secretKey = []
        for i in key:
            if i not in secretKey and i != " ":
                secretKey.append(i)
        message = ""
        for i in s:
            if i != " ":
                message += chr(97 + secretKey.index(i))
            else:
                message += " "
        return message


sln = Solution()

print(sln.decodeMessage(
    "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
