
/**
 * @param {HTMLElement} el - element to be wrapped
 */
function $(el) {

  function css(propertyName, value) {
     el.style[propertyName] = value;
     return this
  }
  this.css = css
  return this
}
