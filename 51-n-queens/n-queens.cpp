class Solution {
public:
    bool IsValid(int i,int j,int n,vector<string>&ans)
    {
        int x=i;
        int y=j;
        while(x>=0)
        {
            if(ans[x][y]=='Q')return false;
            x--;
        }

        x=i;
        y=j;
        while(x>=0 and y>=0)
        {
            if(ans[x][y]=='Q')return false;
            x--;
            y--;
        }
        x=i;
        y=j;
        while(x>=0 and y<=n)
        {
            if(ans[x][y]=='Q')return false;
            x--;
            y++;
        }
        return true;
    }

        void Fun(int row,int n,vector<vector<string>>&grid,vector<string>&ans)
        {
            if(row==n)
            {
                grid.push_back(ans);
                return;
            }
            for(int i=0;i<n;i++)
            {
                if(IsValid(row,i,n,ans))
                {
                    ans[row][i]='Q';
                    Fun(row+1,n,grid,ans);
                    ans[row][i]='.';
                }
            }
        }




    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> grid;
        vector<string> ans;
        for(int i=0;i<n;i++)
        {
            string s;
            for(int j=0;j<n;j++)
            {
                s+=".";
            }
            ans.push_back(s);
        }
        Fun(0,n,grid,ans);
        return grid;
    }
};