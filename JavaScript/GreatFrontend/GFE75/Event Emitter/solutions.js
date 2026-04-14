// You are free to use alternative approaches of
// instantiating the EventEmitter as long as the
// default export has the same interface.

export default class EventEmitter {
  constructor() {
    this.listeners = new Map();
  }
  /**
   * @param {string} eventName
   * @param {Function} listener
   * @returns {EventEmitter}
   */
  on(eventName, listener) {
    if (this.listeners.has(eventName)) {
      this.listeners.get(eventName).push(listener);
    } else {
      this.listeners.set(eventName, [listener]);
    }
    return this;
  }

  /**
   * @param {string} eventName
   * @param {Function} listener
   * @returns {EventEmitter}
   */
  off(eventName, listener) {
    if (this.listeners.has(eventName)) {
      const activeListeners = this.listeners.get(eventName);
      const firstListenerIndex = activeListeners.findIndex(
        (item) => item == listener,
      );
      if (firstListenerIndex >= 0) {
        activeListeners?.splice(firstListenerIndex, 1);
      }
    }
    return this;
  }

  /**
   * @param {string} eventName
   * @param  {...any} args
   * @returns {boolean}
   */
  emit(eventName, ...args) {
    if (this.listeners.has(eventName)) {
      const activeListeners = this.listeners.get(eventName);
      if (activeListeners.length > 0) {
        [...activeListeners].forEach((func) => {
          func.apply(this, args);
        });
        return true;
      }
    }
    return false;
  }
}


const emitter = new EventEmitter();

function addTwoNumbers(a, b) {
    console.log(`The sum is ${a + b}`);
}
emitter.on("foo", addTwoNumbers);
emitter.emit("foo", 2, 5);
// > "The sum is 7"

emitter.on("foo", (a, b) => console.log(`The product is ${a * b}`));
emitter.emit("foo", 4, 5);
// > "The sum is 9"
// > "The product is 20"

emitter.off("foo", addTwoNumbers);
emitter.emit("foo", -3, 9);
// > "The product is -27"
