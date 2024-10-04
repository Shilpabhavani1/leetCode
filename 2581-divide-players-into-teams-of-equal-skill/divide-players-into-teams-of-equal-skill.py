class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # skill.sort()
        # l=[]
        # m=[]
        # a=skill[0]+skill[-1]
        # l.append((skill[0],skill[-1]))
        # m.append((skill[0]*skill[-1]))
        # for i in range(1,len(skill)-1):
        #     s=abs(skill[i]-a)
        #     if s in skill:
        #         if skill[i]+s == a:
        #             l.append((skill[i],s))
        #             m.append((skill[i]*s))
        # n=len(skill)//2
        # # print(m[:n])
        # # se=set(l)
        # # print(m)
        # # print(se)
        # # print(a)
        # print(l)
        # # print(skill)
        # return sum(m[:n])   

        skill.sort()
        s=skill[0]+skill[-1]
        c=0
        for i in range(len(skill)//2):
            if skill[i]+skill[len(skill)-i-1]!=s:
                return -1
            c+= skill[i]*skill[len(skill)-i-1]
        return c    