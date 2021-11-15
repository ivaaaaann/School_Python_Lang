from collections import deque


def bfs(start):
    queue = deque([start])  # 큐 안에 초기값 start(1)을 넣는다
    visited[start] = True  # visited 첫번째 요소를 True로 바꾼다
    while queue:
        v = queue.popleft()  # queue의 맨 처음값 1을 v에 넣는다.
        print(v, end=" ")  # 출력한다.
        for i in graph[v]:  # i에 graph의 맨첫번째 요소를 for문으로 돌면서 넣어준다.
            # 만약 visited i번째 요소가 true(가지 않는것)가 아니라면 큐에 i를 추가(i쪽으로 탐색) 해준다.
            if not visited[i]:
                queue.append(i)
                visited[i] = True  # i는 지나간길로 바꿔준다.


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

bfs(1)
