export default function serializeHTML(root) {
  let lines = [];
  function process(node, depth = 0){
    if(typeof node !== "object"){
        lines.push(`${"\t".repeat(depth)}${node}`)
        return 
    }
    const isArray = Array.isArray(node)
    if(isArray){
        for(const item of node){
            process(item, depth)
        }
    } else {
        lines.push(`${"\t".repeat(depth)}<${node.tag}>`)
        process(node.children, depth+1)
        lines.push(`${"\t".repeat(depth)}</${node.tag}>`)
    }
  }
  process(root)
  return lines.join("\n")
}

const tree = {
    tag: "body",
    children: [
        { tag: "div", children: [{ tag: "span", children: ["foo", "bar"] }] },
        { tag: "div", children: ["baz"] },
    ],
};

console.log(serializeHTML(tree));

// Output:
// `<body>
//   <div>
//     <span>
//       foo
//       bar
//     </span>
//   </div>
//   <div>
//     baz
//   </div>
// </body>`;
