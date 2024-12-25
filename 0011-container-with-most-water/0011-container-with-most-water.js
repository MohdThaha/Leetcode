/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let ans = 0;
    let x=0;
    let y=height.length-1;
    while ( x<y ){
        let l = Math.min(height[x],height[y])
        let b = y-x;
        ans = Math.max(l*b,ans)
        
        if(height[x]<height[y]){
            x++;
        }else{
            y--;
        }
    }
    
    return ans;
};