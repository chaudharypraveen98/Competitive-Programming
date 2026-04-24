

// This is a JavaScript coding problem from BFE.dev 

/**
 * @param {string[][]} message
 * @return {string}
 */
function decode(message) {
    if(message.length===0){
        return ""
    }
    const rowLength = message.length
    const colLength = message[0].length

    function process(dir, row, col){
        if(col === colLength){
            return ''
        }
        const item = message[row][col]
        let nextRow = row + dir;
        let nextDir = dir;
        if(nextRow < 0 || nextRow>= rowLength){
            nextDir *= -1;
            nextRow = row+nextDir
        }
        return item+process(nextDir, nextRow, col+1)
    }
    return process(1, 0, 0)
}

const arr = [
  ['I', 'B', 'C', 'A', 'L', 'K', 'A'],
  ['D', 'R', 'F', 'C', 'A', 'E', 'A'],
  ['G', 'H', 'O', 'E', 'L', 'A', 'D']
];
console.log(decode(arr))

