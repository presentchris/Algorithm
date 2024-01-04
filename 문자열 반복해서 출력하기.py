'''처음 시도한 코드는 출력 결과로 문자열이 옆에 나란히 출력되지 않고 
string
string
string
이렇게 출력 되었음'''
# str, n = input().strip().split(' ')
# n = int(n)
# for i in range(n):
#     print(str)


# 첫 번째 시도한 코드로는 출력할 때 "end=''"를 추가하면 print 함수의 기본 동작인 줄바꿈 대신 아무것도 추가하지 않도록 설정됨
str, n = input().strip().split(' ')
n = int(n)
for i in range(n):
    print(str, end='')


# 두 번째 시도한 코드. n을 정수로 바꾼 후 문자열에 그냥 n을 곱하면 나란히 출력됨
# str, n = input().strip().split(' ')
# print(str*int(n))

  
# 다른 사람의 풀이
# a=input()
# print(a[:-2]*int(a[-1]))
