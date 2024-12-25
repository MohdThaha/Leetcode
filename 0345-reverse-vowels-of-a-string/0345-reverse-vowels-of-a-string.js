/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
     let word = s.split('');
    let start = 0;
    let end = s.length - 1;
    let vowels = "aeiouAEIOU";

    while (start < end) {
        while (start < end && !vowels.includes(word[start])) {
            start++;
        }
        while (start < end && !vowels.includes(word[end])) {
            end--;
        }

        [word[start], word[end]] = [word[end], word[start]];
        start++;
        end--;
    }

    return word.join('');
};
