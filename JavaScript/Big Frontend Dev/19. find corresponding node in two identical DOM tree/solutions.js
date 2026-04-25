
/**
 * @param {HTMLElement} rootA
 * @param {HTMLElement} rootB - rootA and rootB are clone of each other
 * @param {HTMLElement} nodeA
 */
const findCorrespondingNode = (rootA, rootB, target) => {
    function process(node1, node2){
      if(node1===target){
        return node2
      }
      const childs1 = node1.children;
      const childs2 = node2.children;
      for(let i=0; i< childs1.length; i++){
        const res = process(childs1[i], childs2[i]);
        if(res){
          return res
        }
      }
      return null
    }
    return process(rootA, rootB)
}