/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let total = nums.reduce((a, b) => a + b, 0);
    let leftTotal = 0;

    for (let i = 0; i < nums.length; i++) {
        let rightTotal = total - leftTotal - nums[i];

        if (rightTotal === leftTotal) {
            return i;
        }

        leftTotal += nums[i];
    }

    return -1;    
};