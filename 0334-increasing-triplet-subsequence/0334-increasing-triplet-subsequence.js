/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    let x = Infinity; 
    let y = Infinity; 

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] <= x) {
            x = nums[i]; 
        } else if (nums[i] <= y) {
            y = nums[i]; 
        } else {
            return true;
        }
    }

    return false; 
};