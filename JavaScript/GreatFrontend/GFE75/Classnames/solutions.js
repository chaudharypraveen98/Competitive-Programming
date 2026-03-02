/**
 * @param {...(any|Object|Array<any|Object|Array>)} args
 * @return {string}
 */

export default function classNames(...args) {
  let result = [];
  const processArgs = (arg)=>{
    if(!arg) return;

    if(typeof arg==='string' || typeof arg==='number'){
      result.push(arg)
    } else if (Array.isArray(arg)){
      for(const item of arg){
        processArgs(item)
      }
    } else if(typeof arg==='object') {
      // type check prevent date and other types like regex
      // object is only one level nesting
      for(const key of Object.keys(arg)){
        if(key && arg[key]){
          result.push(key)
        }
      }
    }

  }
  for(const arg of args){
    processArgs(arg)
  }
  return result.join(" ")
}
console.log(classNames("foo", "bar")); // 'foo bar'
console.log(classNames("foo", { bar: true })); // 'foo bar'
console.log(classNames({ "foo-bar": true })); // 'foo-bar'
console.log(classNames({ "foo-bar": false })); // ''
console.log(classNames({ foo: true }, { bar: true })); // 'foo bar'
console.log(classNames({ foo: true, bar: true })); // 'foo bar'
console.log(classNames({ foo: true, bar: false, qux: true })); // 'foo qux'
