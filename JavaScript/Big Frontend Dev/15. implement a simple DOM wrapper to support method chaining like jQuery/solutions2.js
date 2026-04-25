class NodeStore {
    constructor(){
        this.DOMStore = Symbol("DomStore")
    }
    has(node){
        return node[this.DOMStore]!== undefined
    }
    set(node, value){
        node[this.DOMStore]= value
    }
    get(node){
        return node[this.DOMStore]|| null
    }
}
const e1 = document.createElement("A");
const e2 = document.createElement("P");
const e3 = document.createElement("DIV");
const e4 = document.createElement("TABLE");
const e5 = document.createElement("A");
const map1 = new NodeStore();
const map2 = new NodeStore();
console.assert(map1.has(e1) === false, "map1 should be empty");
map1.set(e1, "E1 in map1");
console.assert(map1.has(e1) === true, "map1 must have e1");
map2.has(e1);
console.assert(map2.has(e1) === false, "map2 should be empty");
map1.set(e2, 1234);
map1.set(e3, "String");
map1.set(e4, [1, 2, 3, 4]);
console.assert(map1.get(e5, null) === null);
console.assert(map1.get(e5) === undefined);
console.assert(map1.get(e5, 5) === 5);
map1.set(e5, { 1: 2, 3: 4 });
console.assert(map1.get(e1) === "E1 in map1");
console.assert(typeof map1.get(e5) === "object");
