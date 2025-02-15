class Solution:
    def isValid(self, s: str) -> bool:
        
        x = []

        for i in s:
            if i in "({[":  
                x.append(i)  
            elif x and ((i == ')' and x[-1] == '(') or 
                        (i == ']' and x[-1] == '[') or 
                        (i == '}' and x[-1] == '{')):  
                x.pop()  
            else:  
                return False  

        return not x  