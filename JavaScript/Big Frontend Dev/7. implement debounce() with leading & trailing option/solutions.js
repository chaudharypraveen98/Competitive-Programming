

// This is a JavaScript coding problem from BFE.dev 

/**
 * @param {(...args: any[]) => any} func
 * @param {number} wait
 * @param {boolean} option.leading
 * @param {boolean} option.trailing
 * @returns {(...args: any[]) => any}
 */
function debounce(func, wait, option = { leading: false, trailing: true }) {
    let timer = null;

    return function (...args) {
        if(timer) {
          clearTimeout(timer)
        }
        const leading = option.leading && !timer;
        if (leading) {
            func.apply(this, args);
        }
        timer = setTimeout(() => {
            if (option.trailing && !leading) {
                func.apply(this, args);
            }
            timer = null;
        }, wait);
    };
}
