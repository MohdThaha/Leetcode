/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    const n = grid.length;
    const rowMap = new Map();
    let count = 0;

    for (const row of grid) {
        const key = row.join(",");
        rowMap.set(key, (rowMap.get(key) || 0) + 1);
    }

    for (let col = 0; col < n; col++) {
        const colArray = [];
        for (let row = 0; row < n; row++) {
            colArray.push(grid[row][col]);
        }
        const key = colArray.join(",");
        if (rowMap.has(key)) {
            count += rowMap.get(key);
        }
    }

    return count;
};
