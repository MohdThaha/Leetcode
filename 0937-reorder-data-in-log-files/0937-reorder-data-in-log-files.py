class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        num = []

        for i in logs:
            if i.split()[1].isdigit():
                num.append(i)
            else:
                letter.append(i)

        letter.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        
        return letter + num