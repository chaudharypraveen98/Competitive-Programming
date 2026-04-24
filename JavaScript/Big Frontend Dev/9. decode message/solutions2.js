// This is a JavaScript coding problem from BFE.dev

/**
 * @param {string[][]} message
 * @return {string}
 */
function decode(message) {
    if (!message.length || !message[0].length) {
        return "";
    }
    const rowLength = message.length;
    const colLength = message[0].length;

    // Immediate exit for single-row inputs to avoid zigzag logic
    if (rowLength === 1) {
        return message[0].join("");
    }
    let res = "";
    let i = 0,
        j = 0,
        dir = 1;

    while (j < colLength) {
        res += message[i][j];
        j++;
        const nextRow = i + dir;
        // Boundary Check: Flip direction if we hit the top or bottom
        if (nextRow >= rowLength || nextRow < 0) {
            dir *= -1;
        }
        i += dir;
    }
    return res;
}

const arr = [
    ["I", "B", "C", "A", "L", "K", "A"],
    ["D", "R", "F", "C", "A", "E", "A"],
    ["G", "H", "O", "E", "L", "A", "D"],
];
console.log(decode(arr));
