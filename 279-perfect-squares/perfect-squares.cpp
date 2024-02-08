
class Solution

 {
int dp[100001];
public:

    int fun(int n)
    {
        if(n==0) return 0;
        if(dp[n]!=-1)return dp[n];
        int ans=INT_MAX;
        for(int i=1;i*i<=n;i++)
        {
            ans=min(ans,fun(n-i*i)+1);
        }
        return dp[n]=ans;
    }

    int numSquares(int n) {
        memset(dp,-1,sizeof(dp));
        return fun(n);

        
    }
};