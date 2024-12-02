from collections import defaultdict

t = int(input())
for _ in range(t):
    w = input().strip()
    k = int(input())

    n = len(w)
    min_length = float('inf')
    max_length = 0
    found = False

    # 각 문자에 대해 처리
    for char in set(w):
        indices = [i for i, c in enumerate(w) if c == char]
        if len(indices) < k:
            continue

        found = True

        # 최소 길이 계산
        for i in range(len(indices) - k + 1):
            length = indices[i + k - 1] - indices[i] + 1
            min_length = min(min_length, length)

        # 최대 길이 계산
        for i in range(len(indices) - k + 1):
            if w[indices[i]] == char and w[indices[i + k - 1]] == char:
                length = indices[i + k - 1] - indices[i] + 1
                max_length = max(max_length, length)

    if not found:
        print(-1)
    else:
        print(min_length, max_length)
