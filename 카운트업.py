#내 풀이1
def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1, 1):
        answer.append(i)
    return answer

#내 풀이2
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num+1, 1)]

#다른 사람의 풀이1
def solution(start, end):
    return list(range(start, end + 1))

#다른 사람의 풀이2
def solution(start, end):
    answer = []
    while start<=end:
        answer.append(start)
        start+=1
    return answer

#다른 사람의 풀이3
solution = lambda start, end: [i for i in range(start, end+1)]