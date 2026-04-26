
/**
 * @param {any} data
 * @return {string}
 */
function detectType(data) {
  if(data instanceof FileReader) return 'object';
  return Object.prototype.toString.call(data).slice(1, -1).split(' ')[1].toLowerCase();
}