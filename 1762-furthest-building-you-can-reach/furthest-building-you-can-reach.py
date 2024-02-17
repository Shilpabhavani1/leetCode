class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        low=0
        high=n
        def fun(p):
            rbricks=bricks
            l=[]
            for i in range(p):
                if heights[i+1]>heights[i]:
                    l.append(heights[i+1]-heights[i])
            l.sort(reverse=True)
            while l and l[-1]<=rbricks:
                rbricks-=l[-1]
                l.pop()
            return ladders >= len(l)
        while low<high-1:
            mid=low+(high-low)//2
            if fun(mid):
                low=mid
            else:
                high=mid
        return low























        # d=[]
        # for i in range(len(heights)-1):
        #     s=heights[i+1]-heights[i]
        #     if s>0:
        #         d.append(s)
        #         d.sort()
        #         if ladders>0:
        #             ladders-=1
        #         elif bricks>=d[-1]:
        #             bricks-=d.pop()
        #         else:
        #             break
        # return i




            # if heights[i]>=heights[i+1]:
            #     i=i+1
            # if heights[i]<heights[i+1]:
            #     if ladders!=0:
            #         ladders-=1
            #     else:
            #         bricks=heights[i+1]-heights[i]
            # if bricks==0 and ladders==0:
            #     return i