#내 풀이1
def solution(n, k):
    answer = []
    for i in range(k, n+1):
        if i%k==0:
            answer.append(i)
    return answer

#내 풀이2
def solution(n, k):
    return [i for i in range(k,n+1) if i%k==0]

#내 풀이3
solution = lambda n,k: [i for i in range(k,n+1) if i%k==0]

#내 풀이4
def solution(n, k):
    answer=[]
    a=1
    while a <= #n:
        if a%k==0:
            answer.append(a)
        a+=1
    return answer

#다른 사람의 풀이1
def solution(n, k):
    return [i for i in range(k,n+1,k)]

#다른 사람의 풀이2
def solution(n, k):
    answer = []
    index = 1
    while k * index <= n:
        answer.append(k*index)
        index += 1
    return answer

#다른 사람의 풀이3
def solution(n, k):
    return [k*i for i in range(1,n//k+1)]
