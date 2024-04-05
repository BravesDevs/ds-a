class Solution:
    def makeGood(self, s):
        st = []

        for i in s:
            if len(st):
                if i.isupper() and st[-1] == i.lower() or i.islower() and st[-1] == i.upper():
                    st.pop()
                    continue
            st.append(i)
        return ''.join(st)


sln = Solution()
print(sln.makeGood("Pp"))
