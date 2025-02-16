class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        index, step = 0, 1  
        
        for char in s:
            rows[index] += char  # Append character to the current row

            # If at the top or bottom, reverse direction
            if index == 0:
                step = 1  # Move downward
            elif index == numRows - 1:
                step = -1  # Move upward
            
            index += step  # Move to the next row

        return "".join(rows)  # Combine all rows into the final result

        