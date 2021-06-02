from collections import deque

Q=deque()

Q.append(1)
Q.append(2)
Q.append(3)
print(Q)
print(Q.popleft())
print(Q.popleft())