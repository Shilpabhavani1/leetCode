class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in s:
            if st and st[-1]+i in ('AB','CD'):
                st.pop()
            else:
                st.append(i)
        return len(st)
            
        