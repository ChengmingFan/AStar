graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E","F"],
    "E": ["C","D"],
    "F": ["D"]
}
def BFS(graph,start):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)

    while(len(queue) > 0):
        temp = queue.pop(0)
        nodes = graph[temp]
        for w in nodes:
            if w not in visited:
                queue.append(w)
                visited.add(w)
        print(temp)
def DFS(graph,start):
    stack = []
    visited = set()
    stack.append(start)
    visited.add(start)
    while(len(stack) > 0):
        temp = stack.pop()
        nodes = graph[temp]
        for w in nodes:
            if w not in visited:
                stack.append(w)
                visited.add(w)
        print(temp)
visited = set()
def DFS_REC(node):
    print(node)
    visited.add(node)
    for w in graph[node]:
        if w not in visited:
            DFS_REC(w)

if __name__ == '__main__':
    DFS(graph,"A")
    print('-------')
    DFS_REC('A')