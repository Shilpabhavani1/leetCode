class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        r=len(s)-1
        curr=0
        while l<r and s[l]==s[r]:
            curr=s[l]
            while l<=r and s[l]==curr:
                l=l+1
            while r>=l and s[r]==curr:
                r=r-1
        return max(0,r-l+1)

        
        