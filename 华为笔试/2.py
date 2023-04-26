n = 7 
edge = [[0,1], [0,2], [0,3], [0,4], [1,4]]
block = [2,3]
# block = []
# for i in range(m): # m 为读取的障碍物的数量
#     block.append(int(input()))
from collections import defaultdict
import numpy as np 
def generate_tree(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node):
        visited.add(node)
        tree = {}
        for neighbor in graph[node]:
            if neighbor not in visited:
                child_tree = dfs(neighbor)
                tree[neighbor] = child_tree
        return tree
    root = 0
    tree = {root: dfs(root)}
    return tree
tree = generate_tree(edge)
def findpath(tree:defaultdict, blocks:list):
    global min_count, result, path
    result = []
    path = []
    min_count = np.inf
    def traversal(node):
        global min_count, result, path
        if len(node) == 0:
            if len(path) == min_count:
                result.append(path[:])
            elif len(path) < min_count:
                min_count = len(path)
                result = []
                result.append(path[:])
            else:
                pass 
            return 
        for key in node.keys():
            if int(key) in blocks:
                continue
            path.append(int(key))
            traversal(node[key])
            path.pop()
    traversal(tree)
    return result
result = findpath(tree, block)
if len(result) == 1 :
    out = result[0]
    print('->'.join(str(x) for x in out))
elif len(result) > 1:
    result = np.array(result)
    for i in range(len(result[0])):
        tmp = result[:,i]
        idx = np.where(tmp==np.min(tmp))[0]
        if idx.shape[0] == 1:
            break
    out = result[idx[0]]
    print('->'.join(str(x) for x in out))
else:
    print('NULL')
# print(result.join('->'))
            
        
    