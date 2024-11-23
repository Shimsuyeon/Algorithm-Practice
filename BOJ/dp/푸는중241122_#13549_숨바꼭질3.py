from collections import deque
n,k = map(int,input().split())
# n은 수빈이, k는 동생
# 걷는다면 x+1, x-1
# 순간이동 한다면 x*2

# 동생을 찾을 수 있는 가장 빠른 시간

visited = [0 for _ in range(100001)]

def bfs():
    queue = deque([(n,0)])
    visited[n] = 1
    while queue:
        cur,time = queue.popleft()
        if cur == k:
            print(time)
            break
        jump = cur*2
        back = cur-1
        front = cur+1

        if 0<=jump<=100000 and visited[jump]==0:
            queue.append((jump,time))
            visited[jump]=1
        if 0<=back<100000 and visited[back]==0:
            queue.append((back,time+1))
            visited[back]=1
        if 0<=front<100000 and visited[front]==0:
            queue.append((front,time+1))
            visited[front]=1
bfs()