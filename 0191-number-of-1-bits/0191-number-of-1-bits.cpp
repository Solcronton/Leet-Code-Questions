class Solution {
public:
    int hammingWeight(int n) {
        int k=0;
        while(n>0){
            k=k+(n%2);
            n=n/2;
        }
        return k;
        
    }
};