class Solution:
    def calPoints(self, op: List[str]) -> int:

        st = []

        for i in op:
            if i == 'C':
                st.pop()
            elif i == '+':
                st.append(st[-1]+st[-2]) 
            elif i == 'D':
                st.append(st[-1]*2) 
            else:
                st.append(int(i))
        return sum(st) 