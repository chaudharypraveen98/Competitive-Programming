function update(data, command) {
    function process(state, command) {
        if (command.hasOwnProperty("$push")) {
            return [...state].concat(command.$push);
        }
        if (command.hasOwnProperty("$set")) {
            return command.$set;
        }
        if (command.hasOwnProperty("$apply")){
            return command.$apply(state);
        }
        if (command.hasOwnProperty("$merge")){
            if (typeof state !== "object") {
                throw new Error("can't merge");
            }
            return { ...state, ...command.$merge };
        }
        // 2. TRAVERSAL PHASE
        // If it's not a '$' command, we are traversing deeper.
        const isArray = Array.isArray(state);
        const newObj = isArray ? [...state] : { ...state };
        for (const key of Object.keys(command)) {
            newObj[key] = process(
                newObj[key],
                command[key],
            );
        }
        return newObj;
    }
    return process(data, command);
}

const newArr = update([1], { 1: { $set: 2 } });
console.log(newArr);
const state = {
    a: {
        b: {
            c: 1,
        },
    },
    d: 2,
};
const newState = update(state, { a: { b: { c: { $set: 3 } } } });
console.log(newState);

const arr = [1, 2, 3, 4];
const newArr2 = update(arr, { 0: { $apply: (item) => item * 2 } });
console.log(newArr2);

const state2 = {
    a: {
        b: {
            c: 1,
        },
    },
    d: 2,
};
const arr3 = [1, 2, 3, 4];
const newArr3 = update(arr3, { 0: { $set: 0 } });
console.log(newArr3);

const newState2 = update(state2, { a: { b: { $merge: { e: 5 } } } });
console.log(newState2);
