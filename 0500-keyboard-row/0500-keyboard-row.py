class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow = {"q","w","e","r","t","y","u","i","o","p"}
        secondrow = {"a","s","d","f","g","h","j","k","l"}
        thirdrow = {"z","x","c","v","b","n","m"}

        res =[]

        for i in words:
            one = two = three = True
            for j in i:
                word = j.lower()
                if word not in firstrow:
                    one = False
                if word not in secondrow:
                    two = False
                if word not in thirdrow:
                    three = False
            if one == True or two == True or three == True:
                res.append(i)
        return res
        