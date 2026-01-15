class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        dig = ""
        res = []

        for i in digits:
            dig += str(i)
        
        digs = int(dig)
        digs += 1
        dig = str(digs)

        for i in range(len(dig)):
            res.append( int(dig[i]) )

        return res
        