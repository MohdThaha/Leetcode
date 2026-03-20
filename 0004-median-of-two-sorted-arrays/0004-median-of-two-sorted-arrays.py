import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the shorter array for binary search optimization.
        # This simplifies the logic and guarantees log(min(m, n)) complexity.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1) # Length of the shorter array
        n = len(nums2) # Length of the longer array
        
        low = 0
        high = m # partitionX can range from 0 to m (inclusive)
        
        # total_left_elements is the target number of elements in the left partition
        # This formula works for both odd and even total lengths (m+n).
        # E.g., if m+n=5, total_left_elements = 3. Median is max_left.
        # E.g., if m+n=4, total_left_elements = 2. Median is (max_left + min_right)/2.
        total_left_elements = (m + n + 1) // 2 
        
        while low <= high:
            # partitionX is the cut point in nums1.
            # It means 'partitionX' elements from nums1 are in the left partition.
            partitionX = (low + high) // 2
            
            # partitionY is the cut point in nums2.
            # It means 'partitionY' elements from nums2 are in the left partition.
            # The sum of elements in the left partitions must be total_left_elements.
            partitionY = total_left_elements - partitionX
            
            # Determine the four critical values needed for comparison:
            # maxLeftX, minRightX, maxLeftY, minRightY.
            # Use -math.inf and math.inf to handle edge cases where a partition is empty.
            
            # maxLeftX: The last element of nums1's left partition.
            # If partitionX is 0, no elements from nums1 are in the left partition, so maxLeftX is effectively -infinity.
            maxLeftX = -math.inf if partitionX == 0 else nums1[partitionX - 1]
            
            # minRightX: The first element of nums1's right partition.
            # If partitionX is m, all elements from nums1 are in the left partition, so minRightX is effectively +infinity.
            minRightX = math.inf if partitionX == m else nums1[partitionX]
            
            # maxLeftY: The last element of nums2's left partition.
            maxLeftY = -math.inf if partitionY == 0 else nums2[partitionY - 1]
            
            # minRightY: The first element of nums2's right partition.
            minRightY = math.inf if partitionY == n else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # The partition is valid. Calculate the median.
                
                # If the total number of elements (m+n) is even, the median is the average
                # of the two middle elements (max of left half, min of right half).
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    # If the total number of elements (m+n) is odd, the median is the
                    # largest element in the left half.
                    return float(max(maxLeftX, maxLeftY))
            
            # If the partition is not correct, adjust the binary search range:
            elif maxLeftX > minRightY:
                # This means nums1's left partition contains elements that are too large
                # compared to nums2's right partition. We need to move partitionX to the left.
                high = partitionX - 1
            else: # maxLeftY > minRightX
                # This means nums2's left partition contains elements that are too large
                # compared to nums1's right partition. We need to move partitionX to the right.
                low = partitionX + 1
        
        # This line should ideally not be reached given the problem constraints
        # (m+n >= 1, and the binary search is guaranteed to find a partition).
        # It's included for completeness or to handle unexpected states.
        raise ValueError("Input arrays do not satisfy constraints or an unexpected error occurred.")