v = int(input())
ma = [[] for j in range(v)]
e = int(input())
for _ in range(e):
    a= list(map(int, input().split()))
    ma[_] = a


def dfs(ma, v):
    visited = [False] * v
    stack = []
    result = []

    for i in range(v):
        if not visited[i]:
            stack.append(i)
            visited[i] = True

            while stack:
                node = stack.pop()
                result.append(node)

                for neighbor in ma[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        visited[neighbor] = True

    return result
print(dfs(ma, v))





