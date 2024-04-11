class Solution {
public:
    void rotate(vector<int>& arr, int k) {
        int a=k%arr.size();
        reverse(arr.begin(),arr.end());
        reverse(arr.begin(),arr.begin()+a);
        reverse(arr.begin()+a,arr.end());
        
    }
};