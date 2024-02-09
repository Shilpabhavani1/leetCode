class Solution {
public:
    void Fun(int i,vector<int> &nums,vector<int> &res, vector<vector<int>> &ans)
    {
        if(i==nums.size())
        {
            ans.push_back(res);
            return;
        }
        res.push_back(nums[i]);
        Fun(i+1,nums,res,ans);
        res.pop_back();
        Fun(i+1,nums,res,ans);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> res;
        vector<vector<int>> ans;
        Fun(0,nums,res,ans);
        return ans;
        
    }
};