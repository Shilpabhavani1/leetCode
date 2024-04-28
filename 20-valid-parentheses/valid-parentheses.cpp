class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' or s[i]=='{' or s[i]=='[')
            {
                st.push(s[i]);
            }
            else
            {
                if(!st.empty() and ((st.top()=='(' and s[i]==')') or  (st.top()=='{' and s[i]=='}') or  (st.top()=='[' and s[i]==']')))
                {
                    st.pop();
                }
                else
                {
                    return false;
                }
            }
        }
       return st.empty(); 
    }
};