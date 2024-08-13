class Solution {
    vector<vector<int>>res;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int>k;
        sort(candidates.begin(),candidates.end());
        combination(candidates,target,0,k);
        return res;
    }
    void combination(vector<int>& candidates, int target,int idx,vector<int>&k)
    {
            if(target==0)
            {
                res.push_back(k);
                return;
            }
       
        for(int i=idx;i<candidates.size();i++)
        {
            if(candidates[i]>target)break;
            if(i>idx and candidates[i]==candidates[i-1])continue;
            k.push_back(candidates[i]);
            combination(candidates,target-candidates[i],i+1,k);
            k.pop_back();
        }
    }
};