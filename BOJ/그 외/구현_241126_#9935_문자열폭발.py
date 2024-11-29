s = input()
bomb = input()
b = len(bomb)
stack=[]
for el in s:
    stack.append(el)
    if ''.join(stack[-b:])==bomb:
        for _ in range(b):
            stack.pop()

result = ''.join(stack)

if result:
    print(result)
else:
    print("FRULA")