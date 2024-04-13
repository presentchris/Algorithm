# 내 풀이1
solution = lambda my_string,m, c: my_string[c-1::m]

# 내 풀이2
def solution(my_string, m, c):
    ans = ''
    for i in range(c-1, len(my_string), m):
        ans += my_string[i]
    return ans

# 내 풀이3
solution = lambda my_string, m, c: ''.join(my_string[i] for i in range(c-1, len(my_string), m))

# 내 풀이4
def solution(my_string, m, c):
    ans = ''
    i = 0
    while i+c-1 < len(my_string):
        ans += my_string[i+c-1]
        i += m
    return ans

# 다른 사람의 풀이1
def solution(my_string, m, c):
    answer = ''
    for i in range(c-1,len(my_string),m): answer+=my_string[i]
    return answer

# 다른 사람의 풀이2
def solution(my_string, m, c):
    answer = ""
    rows = len(my_string) // m + 1 if len(my_string) % m else len(my_string) // m

    splited_str_list = [my_string[pos*m:(pos+1)*m] for pos in range(rows)]
    for str in splited_str_list:
        answer += str[c-1]

    return answer

# 다른 사람의 풀이3
def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)):
        if i % m == c-1:
            answer += my_string[i]
    return answer
