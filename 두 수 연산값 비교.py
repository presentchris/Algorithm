# 내 풀이
def solution(a, b):
    return max(int(a+b), 2*int(a)*int(b)) if int(a+b)!=2*int(a)*int(b) else int(a+b)

# 다른 사람의 풀이1(if문을 쓰지 않음)
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
