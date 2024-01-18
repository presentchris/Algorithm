# 내 풀이
def solution(a, b):
    return max(int(str(a)+str(b)), int(str(b)+str(a)))

# 다른 사람의 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
