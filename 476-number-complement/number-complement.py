class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)
        # print(b)
        s=""
        for i in range(2,len(b)):
            if b[i]=="0":
                s+="1"
            elif b[i]=="1":
                s+="0"
        # print(s)
        return int(s,2)
        