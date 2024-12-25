/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let ind1 =0;
    let ind2 =0;

    while( ind1<s.length && ind2<t.length){
        if(s[ind1]===t[ind2]){
            ind1++;
        }
        ind2++;

    }

    return ind1 === s.length
    
    
};