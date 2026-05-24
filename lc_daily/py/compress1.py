from ast import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        counters = []
        p1,p2=0,1
        counter = 1
        while p2 < len(chars):
            if chars[p1] == chars[p2]:
                counter += 1
            else:                
                if counter == 1:
                    counters.append(chars[p1])
                else:
                    counters.append(f"{chars[p1]}")
                    # Split the counter into individual characters and append to the list
                    counters.extend(list(str(counter)))
                counter = 1
                p1 = p2
            p2 += 1
        if counter == 1:
            counters.append(chars[p1])
        else:
            counters.append(f"{chars[p1]}")
            counters.extend(list(str(counter)))
        chars[:] = counters
        return len(chars)
    
s=Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))