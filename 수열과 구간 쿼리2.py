#내 풀이1
#1.문법 오류: arr[i]==min(arr[i]), if not answer
#2.타입 오류
#3.query in queries, 다중 for문, max(arr[s:e+1])+1을 변수에 할당하여 arr[i]값을 저장, 더 이상 최소값을 찾을 수 없으면 초기화했던 값과 동일해짐
def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        m = max(arr[s:e+1])+1
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < m:
                m = arr[i]
        if m == max(arr[s:e+1])+1:
            answer.append(-1)
        else:
            answer.append(m)
    return answer

#원본 gpt 풀이
def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        min_value = float('inf')
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < min_value:
                min_value = arr[i]
        if min_value == float('inf'):
            answer.append(-1)
        else:
            answer.append(min_value)
    return answer

#다른 사람의 풀이1
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for i in arr[s:e+1]:
            if i > k:
                tmp.append(i)
        answer.append(-1 if not tmp else min(tmp))
    return answer

#다른 사람의 풀이2
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer

#다른 사람의 풀이3
def solution(arr, queries):
    return list(map(lambda x: -1 if x==10**6 else x, [min(list(filter(lambda x: x > k, arr[s:e+1])) + [10**6]) for s, e, k in queries]))
