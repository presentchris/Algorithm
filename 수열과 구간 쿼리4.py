# 내 풀이1
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

# 내 풀이2
def solution(arr, queries):
    return [arr[i] + sum(1 for s, e, k in queries if i >= s and i <= e and i % k == 0) for i in range(len(arr))]

# 다른 사람의 풀이1_k가 0일 때 오류 발생
def solution(arr, queries):
    for q in queries:
        for i in range((q[0] + q[2] - 1) // q[2] * q[2], q[1] + 1, q[2]):
            arr[i] += 1

    return arr

# 다른 사람의 풀이2
def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        for i in range(s, e+1):
            if not i%k:
                arr[i] += 1
    return arr
