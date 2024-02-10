#내 풀이1
def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer

#내 풀이2
def solution(n):
    answer = [n]
    for _ in range(100):  # 최대 100번의 반복을 가정
        if n == 1:
            break  # n이 1이면 반복 중단
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer

#다른 사람의 풀이1
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer

#다른 사람의 풀이2
def solution(n):
    answer = [n]
    while answer[-1] != 1:
        answer.append(answer[-1]//2) if not answer[-1]%2 else answer.append(answer[-1]*3+1)
    return answer