// This is a JavaScript coding problem from BFE.dev

/**
 * @param {(...args: any[]) => any} func
 * @param {number} wait
 * @param {boolean} option.leading
 * @param {boolean} option.trailing
 * @returns {(...args: any[]) => any}
 */
function throttle(func, wait, option = { leading: true, trailing: true }) {
    let timer = null;
    let lastThis;
    let lastArgs;

    function startTimer() {
        timer = setTimeout(() => {
            if (lastThis && option.trailing) {
                func.apply(lastThis, lastArgs);
                lastArgs = null;
                lastThis = null;
                startTimer();
            } else {
                timer = null;
            }
        }, wait);
    }

    return function (...args) {
        if (timer!==null) {
            lastThis = this;
            lastArgs = args;
        } else {
            if (option.leading) {
                func.apply(this, args);
            }
            startTimer();
        }
    };
}
