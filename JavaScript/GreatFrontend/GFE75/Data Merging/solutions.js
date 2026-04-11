/**
 * @param {Array<{user: number, duration: number, equipment: Array<string>}>} sessions
 * @returns {Array<{user: number, duration: number, equipment: Array<string>}>}
 */
export default function mergeData(sessions) {
    let hashMap = new Map();
    let result = [];

    function deepClone(obj) {
        return {
            ...obj,
            equipment: new Set(obj.equipment),
        };
    }

    sessions.forEach((session) => {
        if (hashMap.has(session.user)) {
            const item = result[hashMap.get(session.user)];
            item.duration += session.duration;
            for (const eq of session.equipment) {
                item.equipment.add(eq);
            }
        } else {
            result.push(deepClone(session));
            const position = result.length - 1;
            hashMap.set(session.user, position);
        }
    });
    result.forEach((resItem) => {
        resItem.equipment = Array.from(resItem.equipment).sort();
    });

    return result;
}

console.log(
    mergeData([
        { user: 8, duration: 50, equipment: ["bench"] },
        { user: 7, duration: 150, equipment: ["dumbbell", "kettlebell"] },
        { user: 8, duration: 50, equipment: ["bench"] },
        { user: 7, duration: 150, equipment: ["bench", "kettlebell"] },
    ]),
);
