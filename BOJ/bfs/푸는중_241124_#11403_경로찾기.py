n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# i,j가 1이면 i->j인 간선 존재한다는 뜻
# i->j 길이가 양수인 경로가 있으면 i,j를 1로
