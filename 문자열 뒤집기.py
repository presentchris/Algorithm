# 내 풀이1
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

# 내 풀이2
solution = lambda my, s, e: my[:s] + my[s:e+1][::-1] + my[e+1:]

# 내 풀이3_for문은 사실 불필요함
def solution(my, s, e):
    for _ in list(my):
        return my[:s] + ''.join(reversed(list(my)[s:e+1])) + my[e+1:] 

# 내 풀이4
def solution(my, s, e):
    return my[:s] + ''.join(reversed(list(my)[s:e+1])) + my[e+1:]

# 내 풀이5
solution = lambda my, s, e: my[:s] + ''.join(reversed(list(my)[s:e+1])) + my[e+1:]

# 다른 사람의 풀이_range를 s, e+1가 아니라 역으로 e, s-1을 쓰고 -1 간격을 두는 방법
def solution(my_string, s, e):
    answer=my_string[:s]
    for i in range(e,s-1,-1):
        answer+=my_string[i]
    answer+=my_string[e+1:]
    return answer
