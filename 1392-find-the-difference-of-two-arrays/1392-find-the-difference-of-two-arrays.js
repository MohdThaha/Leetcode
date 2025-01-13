/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    // Use sets to eliminate duplicates
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    
    // Find numbers unique to nums1
    const uniqueToNums1 = [...set1].filter(num => !set2.has(num));
    
    // Find numbers unique to nums2
    const uniqueToNums2 = [...set2].filter(num => !set1.has(num));
    
    // Return the result as a 2D array
    return [uniqueToNums1, uniqueToNums2];
};
