class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""

        for i in digits:
            digit+=str(i)

        value = int(digit) + 1
        res =[]

        for j in str(value):
            res.append(int(j))
        return res         