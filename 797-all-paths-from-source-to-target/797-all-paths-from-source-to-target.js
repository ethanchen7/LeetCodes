/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    
    const target = graph.length - 1
    const res = []
    
    const queue = []
    queue.push([0])
    
    while (queue.length) {
        
        const path = queue.shift()
        
        const lastNode = path.at(-1)
        
        if (lastNode === target) {
            res.push(path)
            continue
        }
        
        for (let edge of graph[lastNode]) {
            queue.push([...path, edge])
            
        }
    }
    return res
    
};