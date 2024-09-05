class Solution:
    def robotSim(self, commands, obstacles):
        currLocation = (0, 0)
        direction = 1
        turns = [-2, -1]
        for cmd in commands:
            if cmd in turns:
                direction = self.changeDirection(direction, cmd)
            else:
                currLocation = self.moveRobot(currLocation, direction, cmd, obstacles)

        return currLocation[0]**2 + currLocation[1]**2



sln = Solution()
print(sln.robotSim([4,-1,4,-2,4], [[2,4]]))
