# 내 풀이1
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a+d*i
    return answer

# 내 풀이2
def solution(a, d, included):
    return sum(a+d*i for i in range(len(included)) if included[i])

# 내 풀이3
def solution(a, d, included):
    sequence = [a+d*i for i in range(len(included)) if included[i]]
    return sum(sequence)

# 다른 사람의 풀이1_true는 1, false는 0이니까 true만 계산되어지도록 함. 창의적이지만, 단점은 false도 다 계산하기 때문에 코드의 효율성 측면도 살펴야 함.
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

# 다른 사람의 풀이2_enumerate로 included를 인덱스와 값을 i와 f에 가져오고, included가 true, false로 구성되어있어 조건문 걸면 true일 때 for문 앞의 식을 적용
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)
