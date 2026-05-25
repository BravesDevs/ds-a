class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return False
        
        return True