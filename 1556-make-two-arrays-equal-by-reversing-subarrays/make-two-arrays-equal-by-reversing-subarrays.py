class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t=sorted(target)
        a=sorted(arr)
        if t==a:
            return True
        else:
            return False
        