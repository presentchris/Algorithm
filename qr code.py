# 내 풀이1
def solution(q, r, code):
    ans = ''
    for i in range(len(code)):
        if i%q == r:
            ans += code[i]
    return ans

# 내 풀이2
solution = lambda q, r, code: ''.join([code[i] for i in range(len(code)) if i%q ==r])

# 내 풀이3_위 풀이에서 enumerate 추가 사용
def solution(q, r, code):
    ans = ''.join([c for i, c in enumerate(code) if i%q ==r])
    return ans

# 다른 사람의 풀이
def solution(q, r, code):
    return code[r::q]
