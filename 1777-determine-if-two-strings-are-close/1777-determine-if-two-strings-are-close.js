/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) return false;

    // Count character frequencies for both words
    const countFrequency = (word) => {
        const freq = new Map();
        for (const char of word) {
            freq.set(char, (freq.get(char) || 0) + 1);
        }
        return freq;
    };

    const freq1 = countFrequency(word1);
    const freq2 = countFrequency(word2);

    const uniqueChars1 = new Set(freq1.keys());
    const uniqueChars2 = new Set(freq2.keys());
    if (![...uniqueChars1].every((char) => uniqueChars2.has(char))) return false;

    const sortedFreq1 = Array.from(freq1.values()).sort((a, b) => a - b);
    const sortedFreq2 = Array.from(freq2.values()).sort((a, b) => a - b);

    return sortedFreq1.toString() === sortedFreq2.toString();
};
