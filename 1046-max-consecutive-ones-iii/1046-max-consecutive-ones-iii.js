/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let x = 0; 
    let y = 0; 
    let zero = 0; 
    let ans = 0; 

    while (y < nums.length) {
        if (nums[y] === 0) {
            zero++;
        }

        while (zero > k) {
            if (nums[x] === 0) {
                zero--;
            }
            x++; 
        }

        ans = Math.max(ans, y - x + 1);

        y++; 
    }

    return ans;
};