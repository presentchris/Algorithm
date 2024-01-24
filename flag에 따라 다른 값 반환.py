#내 풀이1
def solution(a, b, flag):
    return a+b if flag==True else a-b

#다른 사람의 풀이
def solution(a, b, flag):
    if flag: return a+b
    return a-b

#다른 사람의 풀이2_진짜 창의적이고 수학적이다
def solution(a, b, flag):
    return a + b * (2 * int(flag) - 1)

#다른 사람의 풀이3_flag==True를 쓰지 않고 flag만 있어도 True이니까 OK
def solution(a, b, flag):
    return a + b if flag else a - b