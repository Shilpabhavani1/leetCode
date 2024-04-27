class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        if len(strs)==0:
            return s
        minlen=len(strs[0])
        for i in range(1,len(strs)):
            minlen=min(minlen,len(strs[i]))
        for i in range(0,minlen):
            current=strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i]!=current:
                    return s
            s=s+current
        return s
        