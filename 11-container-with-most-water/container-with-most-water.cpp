class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int start=0;
        int end=n-1;
        int maxarea=INT_MIN;
        while(start<=end)
        {
            if(height[start]<height[end])
            {
                maxarea=max(maxarea,(end-start)*height[start]);
                start++;
            }
            else
            {
                maxarea=max(maxarea,(end-start)*height[end]);
                end--;
            }
            
        }
        return maxarea;
    }
};