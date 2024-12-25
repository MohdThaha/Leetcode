/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
    return (str1 + str2 === str2 + str1) ? str1.substring(0, gcd(str1.length, str2.length)) : "";
};

// calculate the greatest common divisor of two numbers iteratively 
var gcd = function (a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};