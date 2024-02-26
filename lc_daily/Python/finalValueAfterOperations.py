class Sol:
    def finalValueAfterOperations(self, operations):
        X = 0
        operation = {
            "X++": "X+1",
            "X--": "X-1",
            "--X": "X-1",
            "++X": "X+1"
        }
        for op in operations:
            X = eval(operation[op])
        return X


sln = Sol()
print(sln.finalValueAfterOperations(["--X", "X++", "X++"]))
