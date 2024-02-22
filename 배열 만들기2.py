#내 풀이1_다중 if문을 사용한 코드 / in과 not in
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if '0' in str(i) or '5' in str(i):
            if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and '6' not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i):
                answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

#내 풀이2_조건 2개를 and로 연결
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if ('0' in str(i) or '5' in str(i)) and all(j not in str(i) for j in '1,2,3,4,6,7,8,9'):
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

#내 풀이3_다중 for문으로 조건 1개로 줄이고 코드 길이를 줄임 / 1,2,3,4,6,7,8,9를 나열해서 쓰는 방법을 피하려고 했는데 쓰게 됨
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(j not in str(i) for j in '1,2,3,4,6,7,8,9'):
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

#내 풀이4_count 메서드
def solution(l, r):
    answer=[]
    for i in range(l, r+1):
        if all(str(i).count(j)==0 for j in '1,2,3,4,6,7,8,9'):
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

#내 풀이5_find 메서드
def solution(l, r):
    answer=[]
    for i in range(l, r+1):
        if all(str(i).find(j)==-1 for j in '1,2,3,4,6,7,8,9'):
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

#내 풀이6_count를 사용한 리스트컴프리헨션 / 리스트컴프리헨션에서는 answer=[i for 어쩌구] 형식으로 쓰면 i가 리스트에 append 되는 형식이므로 append가 필요없음
def solution(l, r):
    answer = [i for i in range(l, r + 1) if all(str(i).count(j) == 0 for j in '12346789')]
    if not answer:
        answer.append(-1)
    return answer

#내 풀이7_count를 사용한 람다
def solution(l, r):
    answer = list(filter(lambda i: all(str(i).count(j) == 0 for j in '12346789'), range(l, r + 1)))
    if not answer:
        answer.append(-1)
    return answer

#내 풀이8_find를 사용한 리스트컴프리헨션
def solution(l, r):
    answer = [i for i in range(l, r + 1) if all(str(i).find(j) == -1 for j in '12346789')]
    if not answer:
        answer.append(-1)
    return answer


#내 풀이9_find를 사용한 람다
def solution(l, r):
    answer = list(filter(lambda i: all(str(i).find(j) == -1 for j in '12346789'), range(l, r + 1)))
    if not answer:
        answer.append(-1)
    return answer

#내 풀이10_리스트컴프리헨션으로 안 쓸 경우 break,코드를 쪼개보면 다중 for문 원리
def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        for j in '12346789':
            if str(i).count(j) == 0:
                answer.append(i)
                break
    if not answer:
        answer.append(-1)
    return answer

#내 풀이11_3번풀이를 리스트컴프리헨션으로 만들기
def solution(l, r):
    answer = [i for i in range(l, r+1) if all(j not in str(i) for j in '1,2,3,4,6,7,8,9') else -1] 
    if not answer:
        answer.append(-1)
    return answer

#내 풀이12_if not도 리스트컴프리헨션으로 만들기
def solution(l, r):
    answer = [i for i in range(l, r + 1) if all(j not in str(i) for j in '12346789')]
    answer = [-1] if not answer else answer
    return answer

#내 풀이13_3번풀이를 filter와 lambda,list를 사용하여 바꾸기
def solution(l, r):
    answer = list(filter(lambda i: all(j not in str(i) for j in '1,2,3,4,6,7,8,9'), range(l, r+1)))
    if not answer:
        answer.append(-1)
    return answer

#내 풀이14_12번풀이와 동일하지만 변수 대신 return에 else를 사용
def solution(l, r):
    answer = [i for i in range(l, r + 1) if all(j not in str(i) for j in '12346789')]
    return [-1] if not answer else answer

#내 풀이15_람다식으로 한 줄로 끝내기 / ':='는 할당식으로 변수를 할당할 수 있음
solution = lambda l,r: [-1] if not (answer := [i for i in range(l,r+1) if all(j not in str(i) for j in '1,2,3,4,6,7,8,9')]) else answer

#내 풀이16_set이라는 집합 함수가 있다는 것을 뒤늦게 발견
def solution(l, r):
    answer = [i for i in range(l, r + 1) if set(str(i)) <= {'0', '5'}]
    return [-1] if not answer else answer

#내 풀이17_16번풀이를 람다식으로 한 줄로 끝내기
solution = lambda l,r: [-1] if not (answer:=[i for i in range(l, r+1) if set(str(i)) <= {'0','5'}]) else answer

#내 풀이18_뒤늦게 set과 집합연산 및 메서드 공부를 하다가 이렇게도 쓸 수 있다는 것을 알게 됨 / set1.issubset(set2)(set1이 set2의 부분집합인지 확인)
solution = lambda l,r: [-1] if not (answer:=[i for i in range(l, r+1) if set(str(i)).issubset(subset:={'0','5'})]) else answer

#다른 사람의 풀이1_아예 집합으로 만들어서 빼버리는 것의 not
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

#다른 사람의 풀이2
def solution(l, r):
    answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer

#다른 사람의 풀이3
def solution(l, r):
    ret = []
    def f(lim, val):
        if lim == 0:
            ret.append(val)
            return

        f(lim - 1, val * 10 + 5)
        f(lim - 1, val * 10)

    f(6, 0)

    return list(i for i in ret if l <= i <= r)[::-1] or [-1]