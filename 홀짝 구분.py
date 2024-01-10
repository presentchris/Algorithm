# 나의 풀이(f-string은 자동으로 변수를 문자열로 변환하므로 str(a)를 사용하지 않아도 되고 {a}처럼 중괄호만 사용해도 됨)
a = int(input())
print(f'{a} is even') if a%2==0 else print(f'{a} is odd')

# 다른 사람의 풀이1
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")

# 다른 사람의 풀이2(비트 연산자 활용..)
n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")
