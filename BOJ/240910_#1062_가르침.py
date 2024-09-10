import sys
from itertools import combinations

n, k = map(int, input().split())

# 입력받을 때부터 anta, tica 제외
words = [input()[4:-4] for _ in range(n)]

# 5개의 글자는 무조건 배워야 함, 5보다 작으면 어떤 단어도 배울 수 없음
if k < 5:
    print(0)
    sys.exit()

# 필수로 배워야 하는 문자들
must = set('antic')

# 각 단어에서 'antic'에 속하지 않는 문자들을 저장
unique_chars = set()
arr_edit = []

for word in words:
    # 'antic'에 속하지 않는 문자들만 남긴다
    remaining = set(word) - must
    arr_edit.append(remaining)
    unique_chars.update(remaining)
print(arr_edit)
print(unique_chars)
# 남은 알파벳을 배울 수 있는 개수
rest_alpha = k - 5

# 만약 남은 알파벳이 0개이면, 이미 'antic'으로만 읽을 수 있는 단어를 세기
if rest_alpha >= len(unique_chars):
    print(n)
    sys.exit()

# 가능한 조합 중 가장 많은 단어를 읽을 수 있는 조합을 찾음
max_count = 0

# 모든 남은 알파벳 중 rest_alpha 개수만큼 선택하는 조합을 만든다
for comb in combinations(unique_chars, rest_alpha):
    comb_set = set(comb)
    count = 0
    for remaining in arr_edit:
        # 남은 문자들이 모두 comb_set에 포함되어 있으면 단어를 읽을 수 있음
        if remaining <= comb_set:
            count += 1
    max_count = max(max_count, count)

# 결과 출력
print(max_count)