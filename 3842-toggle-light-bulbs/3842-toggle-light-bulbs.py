class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()

        for b in bulbs:
            if b in on:
                on.remove(b)
            else:
                on.add(b)

        return sorted(on)
