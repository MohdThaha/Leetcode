/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let word = s.split(" ");
    let a =[];
    for (let i=s.length-1; i>=0 ;i--){
        if (word[i]) {
        a.push(word[i]);
    }}
    return a.join(" ");
    
};