class Solution {
public:
 void Fun(int i,int j,string &digit,char *ans,vector<string>&res,char keypad[][10])
    {
        if(digit[i]=='\0')
        {
            ans[j]='\0';
            //cout<<ans<<endl;
            if(ans[0]!='\0')res.push_back(ans);
            return;
        }
            int digits=digit[i]-'0';
            for(int k=0;keypad[digits][k];k++)
            {
                ans[j]=keypad[digits][k];
                Fun(i+1,j+1,digit,ans,res,keypad);
            }

        
    }
    vector<string> letterCombinations(string digits) {
        char keypad[][10]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        vector<string>res;
        char ans[100];
        Fun(0,0,digits,ans,res,keypad);
        return res;
        
    }
};