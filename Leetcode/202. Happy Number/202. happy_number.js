var loop_happy = function (n) {
  const str_num = n.toString();
  const square_constants = { 0: 0,1: 1,2: 4,3: 9,4: 16,5: 25,6: 36,7: 49,8: 64,
9: 81,};
  let sum = 0;
  for (let i = 0; i < str_num.length; i++) {
    sum += square_constants[str_num[i]];
  }
  return sum;
};
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n, seen_set = new Set()) {
  if(n===1) return true
  const sq_sum = loop_happy(n, seen_set);
  if(seen_set.has(sq_sum)){
    return false
  }
  seen_set.add(sq_sum)
  return isHappy(sq_sum, seen_set)
};

console.log(isHappy(2))