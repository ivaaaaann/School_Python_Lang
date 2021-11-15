# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 3

# 첫번째 줄에 땅 크기 N, M 1 <=N,  M<= 1000
# 두번째 줄에 N+1 번째 줄까지 땅에 대한 표시이다.
# 0은 물구덩이, 1은 밟아도 무너지지 않는 땅이다.
# 전체 땅속에서 물구덩이 개수를 출력한다.

n, m = map(int, input().split())
graph = []  # 빈 리스트 생성

for i in range(n):
    graph.append(list(map(int, input())))


def puddle(x, y):  # 물 웅덩이 개수 체크
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:  # 물 웅덩이가 있다면
        graph[x][y] = 1
        puddle(x-1, y)
        puddle(x, y-1)
        puddle(x+1, y)
        puddle(x, y+1)
        return True
    else:
        return False


cnt = 0  # 물웅덩이 개수 저장
for i in range(n):
    for j in range(m):
        if puddle(i, j):
            cnt += 1

print(cnt)
