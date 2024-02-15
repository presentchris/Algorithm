#내 풀이1
def solution(n_str):
    return int(n_str)

#내 풀이2_이건 solution함수를 정의하지 않기 때문에 프로그래머스상에서는 에러가 남
lambda n_str: int(n_str)

#다른 사람의 풀이1
solution = int

#다른 사람의 풀이2_'solution = lmabda x : '와 같은 형식으로 써야 함
solution = lambda n_str : int(n_str)
