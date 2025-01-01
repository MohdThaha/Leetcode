/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let x=0;
    let y=0;
    let z=0;
    let ans=0;

    while(y<nums.length){
        if(nums[y]===0){
            z++
        }
        while(z>1){
            if(nums[x]===0){
                z--;
            }
            x++;
        }
        ans = Math.max(ans,y-x)

        y++;

        }
 return ans
    
};