import numpy as np


class Sol:
    def numberOfBeams(self, bank):
        numberOfOnes = [x.count('1') for x in bank if x.count("1") > 0]
        beams = 0
        i, j = 0, 1
        while j < len(numberOfOnes):
            beams += numberOfOnes[i]*numberOfOnes[j]
            i += 1
            j += 1
        return beams


sln = Sol()
print(sln.numberOfBeams(["000", "111", "000"]))
