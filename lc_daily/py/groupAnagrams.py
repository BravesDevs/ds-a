class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
        return list(anagram_dict.values())


sln = Solution()
print(sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
