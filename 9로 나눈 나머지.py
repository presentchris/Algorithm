# 내 풀이
solution = lambda num: int(num)%9

# 다른 사람의 풀이1_map 함수 사용 시 list화 되므로 list를 빼도 무방
def solution(number):
    return sum(list(map(int, number))) % 9

# 다른 사람의 풀이2
def solution(number):
    n=0
    for x in number:
        n+=int(x)
    return n%9
