/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    const target = graph.length - 1
    const res = []
    
    const dfs = (node, path) => {
        
        path.push(node)
        if (node === target) {
            res.push(path)
            return
        }
        
        for (let edge of graph[node]) {
            dfs(edge, [...path])
        }
    }
    
    dfs(0, [])
    return res
};