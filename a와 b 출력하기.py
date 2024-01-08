# 풀이1
a, b = map(int, input().strip().split(' '))
print(r'a =',a,'\nb =',b)


# 다른 사람의 풀이1(따옴표 전 f를 사용했고, 이렇게 하면 변수를 따로 표현할 필요없이 따옴표 안에서 {}를 사용해서 표현하면 됨)
# a, b = map(int, input().strip().split(' '))
# print(f"a = {a}\nb = {b}")

# 다른 사람의 풀이2(아예 메서드 format을 사용하여 괄호 안에 a와 b를 넣어서 표현하는 방식)
# a, b = map(int, input().strip().split(' '))
# print('a = {}\nb = {}'.format(a, b))

