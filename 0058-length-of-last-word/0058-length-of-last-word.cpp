class Solution {
public:
    int lengthOfLastWord(string s) {
        int n=s.length();
        int c=0;
        for (int i=n-1;i>=0;i--) {
            if(s[i]!=' '){
                c+=1;
            }
            else if (c>0){
                break;
            }
        }
        return c;
    }
};