import operator as op

def canConstruct(ransomNote, magazine):
    # TODO: Check for the count of each character in string

    for i in ransomNote:
        if i not in magazine:
            return False
        if op.countOf(ransomNote, i) > op.countOf(magazine, i):
            return False
    return True

    # countRansom = {i:op.countOf(ransomNote, i) for i in set(ransomNote)}
    # countMagazine = {i:op.countOf(magazine, i) for i in set(magazine)}

    # for i in countRansom:
    #     if i not in countMagazine:
    #         return False
    #     if countRansom[i] > countMagazine[i]:
    #         return False

    return True

print(canConstruct("aa", "ab"))