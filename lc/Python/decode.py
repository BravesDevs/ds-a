class Sol:
    def decode(self, encoded, first):
        encoded.insert(0, first)
        for i in range(1, len(encoded)):
            encoded[i] = encoded[i] ^ encoded[i-1]
        return encoded


sln = Sol()

print(sln.decode([6, 2, 7, 3], 4))
