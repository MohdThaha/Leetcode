class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -(2**31)
        if not s:
            return 0

        for i in range(len(s)):
            if s[i] != " ":
                s = s[i:]
                break

        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            sign = 1
        else:
            sign = 1

        for i in range(len(s)):
            if s[i] != "0":
                s = s[i:]
                break

        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break

        if not s:
            return 0
        num = int(s) * sign

        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        else:
            return num