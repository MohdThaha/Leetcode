/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    nums.sort((a,b)=>a-b);

    let ans =0;
    let x =0;
    let y=nums.length-1;

    while(x<y){
        let sum = nums[x]+nums[y];
        if(sum === k){
            ans++;
            x++;
            y--;
        }else if(sum<k){
            x++;
        }else{
            y--;
        }
    }
    return ans;
 
};