/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let ans = {};
    strs.forEach((word)=>{
        const sortedArray = word?.split("").sort()?.join("")
        if(sortedArray in ans){
            ans[sortedArray] = [...ans[sortedArray], word]
        } else {
            ans[sortedArray] = [word]
        }
    })

    return Object.keys(ans).map((item)=>ans[item]);
};

console.log(groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]));