class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        can_eat = n//2
                
        count = Counter(candyType)

        return min( can_eat, len(count) )

        