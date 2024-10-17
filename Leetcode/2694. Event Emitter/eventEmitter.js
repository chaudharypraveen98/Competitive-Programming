class EventEmitter {
  constructor() {
    this.events = {};
  }

  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object}
   */
  subscribe(eventName, callback) {
    if (eventName in this.events) {
      this.events[eventName].push(callback);
    } else {
      this.events[eventName] = [callback];
    }

    return {
      unsubscribe: () => {
        const idx = this.events[eventName].indexOf(callback);
        if (idx !== -1) {
          this.events[eventName].splice(idx, 1);
        }
      },
    };
  }

  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
    let res = [];
    if (eventName in this.events) {
      const listners = this.events[eventName];
      listners.forEach((listner) => {
        res.push(listner(...args));
      });
    }
    return res;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
