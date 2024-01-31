class Solution {
public:
    int Fun(int i,int j,int m,int n,vector<vector<int>>&dp,vector<vector<int>>& A)
    {
        if(i==m-1 and j==n-1)
        {
            return 1;
        }
        if(i>=m || j>=n)
        {
            return 0;
        }
        if(A[i][j]==1)
        {
            return 0;
        }
        if (dp[i][j] != -1) return dp[i][j];
        return dp[i][j]= Fun(i+1,j,m,n,dp,A)+Fun(i,j+1,m,n,dp,A);
    }
    int uniquePathsWithObstacles(vector<vector<int>>& A) {
        int m=A.size();
        int n=A[0].size();
        vector<vector<int>>dp(m,vector<int>(n,-1));
        if(A[m-1][n-1]==1)
        {
            return 0;
        }
        return Fun(0,0,m,n,dp,A);
    }
};