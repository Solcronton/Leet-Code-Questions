class Solution {
public:
    int reverse(int x) {
        int k=0;
        while(x!=0){
            int rem=x%10;
            x=x/10;
            if (k > INT_MAX / 10 || (k == INT_MAX / 10 && rem > 7))
                return 0;

            if (k < INT_MIN / 10 || (k == INT_MIN / 10 && rem < -8))
               return 0;
            k=k*10+rem;
        }
        return k;
        
    }
    
};