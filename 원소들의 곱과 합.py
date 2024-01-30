# 내 풀이1
def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
        if answer > pow(sum(num_list),2):
            return 0
    return 1

# 내 풀이2
def solution(num_list):
    answer = 1
    result = [answer := answer * i for i in num_list]
    return 0 if result[-1] > pow(sum(num_list),2) else 1

# 내 풀이3
def solution(num_list):
    answer = 1
    [answer := answer * i for i in num_list]
    return 0 if answer > pow(sum(num_list),2) else 1

# 내 풀이4
def solution(num_list):
    answer = 1
    return 0 if [answer := answer * i for i in num_list][-1] > pow(sum(num_list),2) else 1

# 내 풀이5
def solution(num_list):
    answer = 1
    return int([answer := answer * i for i in num_list][-1] < pow(sum(num_list),2))

# 다른 사람의 풀이1
def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0

# 다른 사람의 풀이2_이건 좀 창의적. eval() 함수는 문자열을 파이썬 코드로 해석하고 해당 코드를 실행한 결과를 반환. 즉, 문자열로 변환한 다음 join을 통해 문자열을 *로 연결한 후, 문자열로 표현된 수식을 계산.
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

