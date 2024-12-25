/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let write = 0; 
    let read = 0;  

    while (read < chars.length) {
        const char = chars[read]; 
        let count = 0;

        while (chars[read] === char) {
            read++;
            count++;
        }


        chars[write] = char;
        write++;

        if (count > 1) {
            for (const digit of count.toString()) {
                chars[write] = digit;
                write++;
            }
        }
    }

    return write; 
};
