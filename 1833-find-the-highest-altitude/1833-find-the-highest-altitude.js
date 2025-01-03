/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let ans =0;
    let x = 0;
    let y = 0;
    
    while(x<gain.length){
        y+=gain[x]
        x++;
        ans = Math.max(ans,y)
    }
    return ans
};