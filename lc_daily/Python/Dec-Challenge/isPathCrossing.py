import copy


class Sol:
    def isPathCrossing(self, path):
        position = [0, 0]
        visited = [[0, 0]]
        movement = {
            'N': 1,
            'S': -1,
            'E': 1,
            'W': -1
        }

        for i in path:
            if i == 'N' or i == 'S':
                position[0] = position[0]+movement[i]
            else:
                position[1] = position[1]+movement[i]

            if position in visited:
                return True

            visited.append(copy.deepcopy(position))
        return False


sln = Sol()
print(sln.isPathCrossing("NESWW"))
