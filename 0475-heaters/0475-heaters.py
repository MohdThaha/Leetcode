from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0

        for house in houses:
            left, right = 0, len(heaters) - 1
            nearest = float('inf')

            while left <= right:
                mid = (left + right) // 2
                dist = abs(heaters[mid] - house)
                nearest = min(nearest, dist)

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            max_radius = max(max_radius, nearest)

        return max_radius
