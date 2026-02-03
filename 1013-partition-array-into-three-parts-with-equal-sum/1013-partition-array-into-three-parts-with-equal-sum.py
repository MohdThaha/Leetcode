class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        oneThird = total // 3
        twoThird = oneThird * 2

        prefixSum = 0
        foundFirst = False

        for i in range(len(arr) - 1):  
            prefixSum += arr[i]

            if prefixSum == oneThird and not foundFirst:
                foundFirst = True
            elif prefixSum == twoThird and foundFirst:
                return True

        return False
