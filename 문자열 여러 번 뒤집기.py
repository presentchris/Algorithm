# 내 풀이1_reversed 이용해 뒤집기 / lst.reverse()는 사용하기에 제한적(괄호 안에 아무 인자도 넣을 수 없음, 특정부분만 뒤집기 제한적)
def solution(my_string, queries):
    lst = list(my_string) 
    for s,e in queries:
        part = reversed(lst[s:e+1])
        lst[s:e+1] = part
    return ''.join(lst)

# 내 풀이2_part변수 없애고 슬라이싱을 이용해 뒤집기
def solution(my_string, queries):
    lst = list(my_string) 
    for s,e in queries:
        lst[s:e+1] = lst[s:e+1][::-1]
    return ''.join(lst)

# 내 풀이3_gpt의 신박한 풀이
def solution(my_string, queries):
    lst = list(my_string) 
    for s,e in queries:
        lst = lst[:s] + lst[s:e+1][::-1] + lst[e+1:]
    return ''.join(lst)

# 다른 사람의 풀이1
def solution(s,q):
    s=[*s]
    for t in q:a,b=t;s[a:b+1]=s[a:b+1][::-1]
    return ''.join(s)
