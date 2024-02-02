class Solution {
public:
    int dp[100001];
    int fun(int n)
    {
        if(n<=1)return n;
        if(dp[n]!=-1)return dp[n];
        return dp[n]=fun(n-1)+fun(n-2);
        
    }
    int fib(int n) {
        memset(dp,-1,sizeof(dp));
        return fun(n);
       
        
    }
};
    // int fib(int n) {
    //     if(n==0 or n==1)
    //     {
    //         return n;
    //     }
    //     return fib(n-1)+fib(n-2);
        
    // }
