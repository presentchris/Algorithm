# 내 풀이1
def solution(start, end):
    return [i for i in range(start, end-1, -1)]

# 내 풀이2
solution = lambda s, e: [i for i in range(s, e-1, -1)]

# 내 풀이3
def solution(start, end):
    log = [i for i in range(end, start+1)]
    ans = list(reversed(log))
    return ans

# 내 풀이4
def solution(start, end):
    log = [i for i in range(end, start+1)]
    ans = log[::-1]
    return ans

# 다른 사람의 풀이1
def solution(start, end):
    return list(range(start,end-1,-1))

# 다른 사람의 풀이2
def solution(start, end):
    answer = []
    while start>=end:
        answer.append(start)
        start-=1        
    return answer

# 다른 사람의 풀이3
def solution(start, end):
    answer = []
    for i in range(start,end-1,-1):
        answer.append(i)
    return answer
