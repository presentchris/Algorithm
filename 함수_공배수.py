#1
def solution(number, n, m):
    answer = 0
    if (number%n==0) and (number%m==0):
        return 1
    return answer


#2
#def solution(number, n, m):
#    answer = 0
#    if (number%n==0) and (number%m==0):
#        answer = 1
#    else:
#        answer = 0
#    return answer



#다른 사람의 풀이1('=='의 결과는 이미 bool로 나오기 때문에 bool로 변경할 필요없다는 점도 참고)
#def solution(number, n, m):
#    return int(bool(number % n == 0) & bool(number % m == 0))


#다른 사람의 풀이2
#def solution(number, n, m):
#    return 1 if number%n==0 and number%m==0 else 0


#다른 사람의 풀이3
#def solution(number, n, m):
#    if number%n and number%m: return 0
#    return 1