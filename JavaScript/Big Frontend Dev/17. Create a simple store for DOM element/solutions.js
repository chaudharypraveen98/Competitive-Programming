class NodeStore {
    constructor() {
        this.indexSet = new Set();
        this.map = {};
    }
    /**
     * @param {Node} node
     * @param {any} value
     */
    set(node, value) {
        const key = JSON.stringify(node);
        this.indexSet.add(key);
        this.map[key] = value;
    }
    /**
     * @param {Node} node
     * @return {any}
     */
    get(node) {
        const key = JSON.stringify(node);
        if (this.indexSet.has(key)) {
            return this.map[key];
        } else {
            throw new Error("Key not found");
        }
    }

    /**
     * @param {Node} node
     * @return {Boolean}
     */
    has(node) {
        const key = JSON.stringify(node);
        return this.indexSet.has(key);
    }
}

const map = new NodeStore();
map.set("test", 1234);
console.log(map.get("test"));
