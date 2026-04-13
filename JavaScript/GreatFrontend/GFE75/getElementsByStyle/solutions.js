/**
 * @param {Element} element
 * @param {string} property
 * @param {string} value
 * @return {Array<Element>}
 */
export default function getElementsByStyle(element, property, value) {
  let results = [];

  function traverse(node) {
    for (const child of node.children) {
      if (window.getComputedStyle(child).getPropertyValue(property) === value) {
        results.push(child);
      }
      traverse(child);
    }

    return results;
  }
  traverse(element);
  return results;
}

const doc = new DOMParser().parseFromString(
  `<div>
    <span style="font-size: 12px">Span</span>
    <p style="font-size: 12px">Paragraph</p>
    <blockquote style="font-size: 14px">Blockquote</blockquote>
  </div>`,
  'text/html',
);

getElementsByStyle(doc.body, 'font-size', '12px');
// [span, p] <-- This is an array of elements.
