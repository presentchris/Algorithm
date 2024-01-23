#내 풀이1_eval를 쓰지 않으면 에러가 난다. eval은 파이썬의 내장 함수 중 하나로, 문자열로 표현된 파이썬 코드를 실행하여 결과를 반환하는 역할을 한다고 하는데 계속 사용해보면서 감을 익혀야겠음 예시를 봐도 어떨 때 쓰는 건지 완벽히 이해를 못함
def solution(ineq, eq, n, m):
    return int(eval(f'{n} {ineq} {m}')) if eq=='!' else int(eval(f'{n} {ineq}{eq} {m}'))

#내 풀이2
def solution(ineq, eq, n, m):
    if eq=='!':
        return int(eval(f'{n} {ineq} {m}'))
    return int(eval(f'{n} {ineq}{eq} {m}'))

#GPT 풀이
def solution(ineq, eq, n, m):
    if (ineq == "<" and eq == "=" and n <= m) or (ineq == ">" and eq == "=" and n >= m) or (ineq == "<" and eq == "!" and n < m) or (ineq == ">" and eq == "!" and n > m):
        return 1
    return 0

#다른 사람의 풀이1_똑같이 eval을 사용했지만, eq를 공백으로 대체한게 특징. 나도 이 방법을 시도 했었지만 return을 써서 결과가 달랐다. return을 쓰지 않고 그냥 eq=''를 써야 함
def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n} {ineq}{eq} {m}'))

#다른 사람의 풀이2_eq에 replace를 쓴 답안. 메서드를 익히고 잘 활용해야겠다는 생각이 듦. 그리고 나도 str에 더하는 것까지는 생각해봤는데 여기서 바로 int를 씌웠더니 안 됐다. eval를 한 다음에 int를 씌워야 한다.
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))