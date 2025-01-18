/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) return false;

    const count1 = new Array(26).fill(0);
    const count2 = new Array(26).fill(0);
    const seen1 = new Set();
    const seen2 = new Set();

    for (let char of word1) {
        const index = char.charCodeAt(0) - 97;
        count1[index]++;
        seen1.add(index);
    }
    for (let char of word2) {
        const index = char.charCodeAt(0) - 97;
        count2[index]++;
        seen2.add(index);
    }

    if (seen1.size !== seen2.size || ![...seen1].every((char) => seen2.has(char))) {
        return false;
    }

    count1.sort((a, b) => a - b);
    count2.sort((a, b) => a - b);

    return count1.join('') === count2.join('');
};
