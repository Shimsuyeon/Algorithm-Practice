def min_height_to_light(N, M, positions):
    # 이진 탐색을 위한 초기값
    left, right = 0, N
    result = N  # 최소 높이를 저장할 변수

    # 가로등 위치를 정렬
    positions.sort()

    while left <= right:
        mid = (left + right) // 2  # 높이 h를 중간값으로 설정
        current_coverage = 0  # 현재 덮인 구간의 끝

        for pos in positions:
            if current_coverage < pos - mid:
                # 현재 구간이 덮이지 않음
                break
            current_coverage = pos + mid

        if current_coverage >= N:
            # 모든 구간이 덮였다면 높이를 줄여본다
            result = mid
            right = mid - 1
        else:
            # 덮이지 않았다면 높이를 늘려야 함
            left = mid + 1

    return result

# 입력 예제
N = int(input())
M = int(input())
positions = list(map(int,input().split()))
print(min_height_to_light(N, M, positions))  # 결과: 최소 높이
