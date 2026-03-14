class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        st = []

        for t in tokens:
            if t not in ops:
                st.append(int(t))
            else:
                x = st.pop()
                y = st.pop()

                if t == "+":
                    st.append(y + x)
                elif t == "-":
                    st.append(y - x)
                elif t == "*":
                    st.append(y * x)
                elif t == "/":
                    st.append(int(y / x))  
        return st.pop()