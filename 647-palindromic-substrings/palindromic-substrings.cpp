class Solution {
public:
    bool Pali(string s)
    {
        int i=0;
        int j=s.size()-1;
        while(i<j){
        if(s[i]!=s[j])return 0;
        i++;j--;
        }
        return 1;
    }
    int countSubstrings(string s) {
        int c=0;
        for(int i=0;i<s.size();i++)
        {
             string p="";
            for(int j=i;j<s.size();j++)
            {
                p+=s[j];
                if(Pali(p))c++;
                
            }
        }
        return c;
    }
};