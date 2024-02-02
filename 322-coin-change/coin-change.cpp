class Solution {
public:
    #define ll long long 
    int dp[100001];
    ll Coinchange(vector<int>& coins, ll amount , ll n)
    {
        if(amount==0)return 0;
        // if(amount<0)return INT_MAX;
        if(dp[amount]!=-1)return dp[amount];
        ll ans=INT_MAX;
        for(int i=0;i<n;i++)
        {
            if(coins[i]<=amount)
            {
                ans=min(ans,1+Coinchange(coins,amount-coins[i],n));
            }
        }
        return dp[amount]=ans;
    }

    int coinChange(vector<int>& coins, int amount) {
        ll n=coins.size();
        memset(dp,-1,sizeof(dp));
        int ans=Coinchange(coins,amount,n);
        if(ans==INT_MAX)return -1;
        return ans;
        
    }
};