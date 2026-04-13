/**
 * @param {Element} element
 * @param {string} classNames
 * @return {Array<Element>}
 */
export default function getElementsByClassName(element, classNames) {
  let results = [];
  const targetClasses = classNames.trim().split(" ").filter(Boolean);;
  if (targetClasses.length === 0) {
    return [];
  }

  function traverse(node) {
    for (const child of node.children) {
      if (targetClasses.every((classItem) => child.classList.contains(classItem))) {
        results.push(child);
      }
      traverse(child);
    }
  }
  traverse(element);
  return results;
}


const doc = new DOMParser().parseFromString(
  `<div class="foo bar baz">
    <span class="bar baz">Span</span>
    <p class="foo baz">Paragraph</p>
    <div class="foo bar"></div>
  </div>`,
  'text/html',
);

getElementsByClassName(doc.body, 'foo bar');