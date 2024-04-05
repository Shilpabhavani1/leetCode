class Solution:
    def makeGood(self, s: str) -> str:
        st = []  
        for char in s:
            if st and abs(ord(char) - ord(st[-1])) == 32:
                st.pop()
            else:
                st.append(char)

        return ''.join(st)