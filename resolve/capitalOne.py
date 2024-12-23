class Solution:
    def resolve(self, commands):
        stack = []
        triggered = {
            "cp": 0,
            "ls": 0,
            "mv": 0
        }
        cmds = ["cp", "ls", "mv"]
        for i in commands:
            if i in cmds:
                stack.append(i)
                triggered[i] += 1
            else:
                i = int(i.replace("!", ""))
                cmd = stack[i-1]
                stack.append(cmd)
                triggered[cmd] += 1
        return list(triggered.values())


sln = Solution()
print(sln.resolve(["ls", "cp", "mv", "mv", "mv", "!1", "!3", "!6"]))
