#내 풀이1
def solution(my_string, n):
    answer = ''
    idx = 0
    while idx < n:
        answer += my_string[idx]
        idx += 1
    return answer

#내 풀이2
def solution(my_string, n):
    answer = ''
    for i in range(0, n):
        answer += my_string[i]
    return answer

#내 풀이3
def solution(my_string, n):
    return ''.join(my_string[i] for i in range(0,n))

#내 풀이4
solution = lambda my_string, n : ''.join(my_string[i] for i in range(0,n))

#다른 사람의 풀이1
def solution(my_string, n):
    return my_string[:n]

#다른 사람의 풀이2
def solution(my_string, n):
    return my_string[0:n]

#다른 사람의 풀이3
def solution(my_string, n):
    answer = my_string[:n]
    return answer