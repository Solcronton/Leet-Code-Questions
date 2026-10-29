class Solution {
public:
    int maxArea(vector<int>& height) {
        int c=0;
        int l=0;
        int r= height.size()-1;

        while(r>l){
            int w=r-l;
            int h=min(height[l],height[r]);
            int area=w*h;
            if(area>c){
                c=area;
            }
            if(height[l]<height[r]){
                l++;
            }else{
                r--;
            }
        }
        return c;
        
        
        
    }
};