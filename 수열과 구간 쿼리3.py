#내 풀이1_gpt도움
def solution(arr, queries):
    answer = []
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    answer.extend(arr)
    return answer

#내 풀이2
def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr

#gpt의 풀이_슬라이싱을 사용하여 리스트의 요소 교환
def solution(arr, queries):
    for i, j in queries:
        arr[i:i+1], arr[j:j+1] = arr[j:j+1], arr[i:i+1]
    return arr

#다른 사람의 풀이1
def solution(arr, queries):
    answer = []
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return arr

#다른 사람의 풀이2
def solution(arr, queries):
    for query in queries:
        temp = arr[query[1]]
        arr[query[1]] = arr[query[0]]
        arr[query[0]] = temp
    return arr
