/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let ans = 0;
    let count = 0;

    for (let i = 0; i < k; i++) {
        if (isVowel(s[i])) {
            count++;
        }
    }
    ans = Math.max(ans, count);


     // Slide the window and update the count
    for (let i = k; i < s.length; i++) {
        if (s[i] === 'a' || s[i]  === 'e' || s[i]  === 'i' || s[i]  === 'o' || s[i]  === 'u') {
            count++;
        }
        if (isVowel(s[i - k])) {
            count--;
        }
        ans = Math.max(ans, count);
    }

    return ans;
};


function isVowel(c) {
    return c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
}
