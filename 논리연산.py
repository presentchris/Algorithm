# 내 풀이1
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

# 내 풀이2
solution = lambda x1, x2, x3, x4: (x1 or x2) and (x3 or x4)

# 다른 사람의 풀이1
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

# 다른 사람의 풀이2
def solution(x1, x2, x3, x4):
    return cal(cal(x1, x2, 1), cal(x3, x4, 1), 0)

def cal(x,y,flag):
    if flag:
        if True in [x, y]:
            return True
        else:
            return False
    else:
        if False in [x, y]:
            return False
        else:
            return True
