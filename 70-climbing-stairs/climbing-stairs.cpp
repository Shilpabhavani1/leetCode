class Solution {
public:
    int dp[1000];
    int stairs(int n)
    {
        if(n==1)return n;
        if(n==2)return n;
        if(dp[n]!=-1)return dp[n];
        return dp[n]=stairs(n-1)+stairs(n-2);
        
    }
    int climbStairs(int n) {
        memset(dp,-1,sizeof(dp));
        return stairs(n);
       
        
    }
};