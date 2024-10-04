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
        total_sum = skill[0] + skill[-1]  # Fixed sum for all pairs
        n = len(skill)
        chemistry_sum = 0

        # Iterate through the sorted list, pairing smallest and largest
        for i in range(n // 2):
            # Pair the smallest (i) and largest (n-i-1)
            if skill[i] + skill[n - i - 1] != total_sum:
                return -1  # If any pair doesn't sum to the fixed value, return -1
            chemistry_sum += skill[i] * skill[n - i - 1]  # Add the product to the total chemistry sum

        return chemistry_sum     