import sys

n, k = map(int, input().split())

arr = [[list(str(input()))] for _ in range(n)]

if k < 5:
    print(0)
    sys.exit()

# arr에서 앞부분 alpha, 뒷부분 tica 제외

for i in range(n):
    arr[i] = arr[i][0][4:-4]

must = ['a', 'c', 'i', 'n', 't']

# a, c, i, n, t에 해당하면 삭제
arr_edit = [[] for _ in range(n)]
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] not in must and arr[i][j] not in arr_edit[i]:
            arr_edit[i].append(arr[i][j])

#arr_edit 원소 개수 적은 순으로 sort
arr_edit.sort(key = lambda x: len(x))

result_list = []
rest_alpha = k - 5
result=0

for i in range(n):
    word_len = len(arr_edit[i])
    word_comp = 0
    word_list = []
    for j in arr_edit[i]:
        # print(j)
        if j in result_list:
            word_comp+=1
        elif j not in result_list and rest_alpha>0:
            word_comp+=1
            word_list.append(j)
    if word_len == word_comp:
        result_list+=word_list
        rest_alpha-=word_len
        result+=1
# print(result_list)
print(result)
        