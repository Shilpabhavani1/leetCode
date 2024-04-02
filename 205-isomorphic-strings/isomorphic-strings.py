class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False


















# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         d={}
#         d1={}
#         l=[]
#         k=[]
#         a=list(s)
#         b=list(t)
#         for i in range(len(a)):
#             if a[i]==b[i]:
#                 return False
#         print(a)
#         print(b)
#         for i in s:
#             if i not in d:
#                 d[i]=1
#             else:
#                 d[i]+=1
#         # print(d)
#         for i in t:
#             if i not in d1:
#                 d1[i]=1
#             else:
#                 d1[i]+=1
#         # print(d1)
#         for i,j in d.items():
#             # print(j)
#             l.append(j)
#         print(l)
#         for i,j in d1.items():
#             # print(j)
#             k.append(j)
#         print(k)
#         if l==k:
#             return True
#         return False






#         # s1=set(s)
#         # s2=set(t)
#         # if len(s1)==len(s2):
#         #     return True
#         # return False       