# 내 풀이1
n = int(input())
for i in range(1, n+1):
    ans = '*' * i
    print(ans)


# 내 풀이2
n = int(input())
for i in range(1, n+1):
    print('*' * i)


# 내 풀이3
n = int(input())
i = 1
while i <= n:
    print('*' * i)
    i += 1


# 내 풀이4
n = int(input())
ans = ['*' * i for i in range(1, n+1)]
print("\n".join(ans))


# 내 풀이5
n = int(input())
print("\n".join(map(lambda x: '*' * x, range(1, n+1))))


# 다른 사람의 풀이1
print('\n'.join('*' * (i + 1) for i in range(int(input()))))


# 다른 사람의 풀이2
n = int(input())
for i in range(n):
    print('*'*(i+1))


# 다른 사람의 풀이3
n = int(input())
for i in range(1,n+1):
    temp = ''
    for j in range(i):
        temp += '*'
    print(temp)
#print(n)


# 다른 사람의 풀이4
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print('*', end = '')
    print()
