import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1) 
        n = len(nums2) 
        
        low = 0
        high = m 
        
        total_left_elements = (m + n + 1) // 2 
        
        while low <= high:
            partitionX = (low + high) // 2
            
            partitionY = total_left_elements - partitionX
            
            maxLeftX = -math.inf if partitionX == 0 else nums1[partitionX - 1]
            
            minRightX = math.inf if partitionX == m else nums1[partitionX]
            
            maxLeftY = -math.inf if partitionY == 0 else nums2[partitionY - 1]
            
            minRightY = math.inf if partitionY == n else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            
            elif maxLeftX > minRightY:
            
                high = partitionX - 1
            else:
                low = partitionX + 1
        