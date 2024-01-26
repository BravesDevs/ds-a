class Solution:
    def uniqueMorseRepresentations(self, words):
        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..'}
        uniqueCodes = set()
        for i in words:
            st = ""
            for j in i:
                st += MORSE_CODE_DICT[j.upper()]
            uniqueCodes.add(st)

        return len(uniqueCodes)


sln = Solution()
print(sln.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
