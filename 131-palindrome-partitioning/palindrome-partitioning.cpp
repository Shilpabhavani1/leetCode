class Solution {
public:
    void fun(int ind,int n,string &s,vector<vector<string>>&res,vector<string>&temp)
    {
        if(ind==n)
        {
            res.push_back(temp);
            return;
        }
        for(int i=ind;i<n;i++)
        {
            string str=s.substr(ind,i-ind+1);
            if(str==string(str.rbegin(),str.rend()))
            {
                temp.push_back(str);
                fun(i+1,n,s,res,temp);
                temp.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> temp;
        int n=s.size();
        fun(0,n,s,res,temp);
        return res;

        
    }
};