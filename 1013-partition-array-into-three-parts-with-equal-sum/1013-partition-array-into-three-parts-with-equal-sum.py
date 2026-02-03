class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        currentSum = 0
        result = []

        for i in arr:
            currentSum += i
            result.append(currentSum)
        
        finalSum = result[-1]
        oneThird = finalSum//3
        twoThird = oneThird*2
        foundFirst = False

        if finalSum % 3 != 0:
            return False

        for i in result[:-1]:
            if i == oneThird and not foundFirst:
                foundFirst = True
            elif i == twoThird and foundFirst:
                return True
            
        return False