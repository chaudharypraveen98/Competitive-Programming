
/**
 * @param {any} data
 * @return {string}
 */
function detectType(data) {
  if(data instanceof FileReader) return 'object';
  const type = Object.prototype.toString.call(data);
  return type.slice(8, -1).toLowerCase();
}