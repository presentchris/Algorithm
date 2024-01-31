# 내 풀이1
def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if i%2==0:
            even += str(i)
        else:
            odd += str(i)
    return int(even) + int(odd)

# 내 풀이2
def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if i%2==0:
            even += ''.join(str(i))
        else:
            odd += ''.join(str(i))
    return int(even) + int(odd)

# 내 풀이3_삼항 조건 연산자 / 리스트 컴프리헨션을 쓸 경우에는 += 형식을 쓸 수 없고, ''.join()과 같이 써야 함
def solution(num_list):
    even = ''.join(str(i) for i in num_list if i%2==0)
    odd = ''.join(str(i) for i in num_list if i%2!=0)
    return int(even) + int(odd)

# 내 풀이4_아예 int()로 묶기 + bool도 써 봄
def solution(num_list):
    return int(''.join(str(o) for o in num_list if bool(o%2))) + int(''.join(str(e) for e in num_list if e%2==0))

# 다른 사람의 풀이1_리스트로 초기화해서 append하는 방식은 익숙하지 않은데 다음에 한 번 시도해 봐야겠다
def solution(num_list):
    o=[]
    e=[]
    for n in num_list:
        if n%2:o.append(str(n))
        else:e.append(str(n))
    return int(''.join(o))+int(''.join(e))

# 다른 사람의 풀이2_if not 처음 봤다, 나랑은 다르게 for문 리스트 컴프리헨션이라 []로 묶었는데 이게 정석같다
def solution(num_list):
    return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))
