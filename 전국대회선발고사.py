# 내 풀이1_틀린 풀이
def solution(rank, attendance):
    tmp=[]
    for i in range(len(attendance)):
        if attendance[i]:
            tmp.append(rank[i])
    abc=sorted(tmp)[:3]
    a,b,c = abc
    return 10000*a+100*b+c

# 내 풀이2_고친 정답 풀이, 학생의 등수를 a,b,c에 할당하는 것이 아니라 학생 번호(인덱스=순서 번호)를 a,b,c에 할당하는 것이었기 때문에 계산이 다르게 나옴. 문제 똑바로 보기.
def solution(rank, attendance):
    tmp = []
    for i in range(len(attendance)):
        if attendance[i]:
            # 참여 가능한 학생의 등수를 추가
            tmp.append((rank[i], i))  # (등수, 학생 번호) 튜플 추가
    # 등수에 따라 정렬
    abc = sorted(tmp, key=lambda x: x[0])[:3]
    # 학생 번호 추출
    a, b, c = [x[1] for x in abc]  # 학생 번호 기준으로 수정
    return 10000*a + 100*b + c

# 내 풀이3_코드 줄이기
def solution(rank, attend):
    a, b, c = [x[1] for x in sorted([(rank[i], i) for i in range(len(attend)) if attend[i]], key=lambda x: x[0])[:3]]
    return 10000*a + 100*b + c

# gpt 풀이
def solution(rank, attendance):
    # 참석 가능한 학생들의 등수와 그들의 번호를 담을 리스트를 생성. enumerate는 반복 가능한(iterable) 객체(예: 리스트, 튜플, 문자열 등)를 순회할 때, 각 요소와 함께 그 위치의 인덱스를 제공. i는 enumerate() 함수에 의해 생성된 인덱스를 받아옴. enumerate 함수는 순회하는 반복 가능한 객체의 각 요소에 대해 인덱스와 값을 함께 제공합니다. 이 때, 반환되는 값은 (인덱스, 값) 형태의 튜플이기 때문에 i가 먼저 선언되고 튜플인(r, attend)가 오게 됨.
    available_students = [(r, i) for i, (r, attend) in enumerate(zip(rank, attendance)) if attend]
    # 참석 가능한 학생들을 등수에 따라 오름차순으로 정렬. x는 available_students 리스트의 요소를 의미하며 x[0]은 r인 등수.
    sorted_students = sorted(available_students, key=lambda x: x[0])    
    # 정렬된 리스트에서 상위 3명의 학생 번호를 가져옴. sorted_students는 available_students를 등수에 따라 정렬한 것. x[0]은 등수, x[1]은 학생 번호로 되어 있음. student[1]은 상위 3등에 해당하는 학생의 '번호'가 됨.
    a, b, c = [student[1] for student in sorted_students[:3]]   
    # 문제에서 요구하는 형식으로 번호를 조합하여 반환.
    return 10000 * a + 100 * b + c

# gpt 코드 줄이기
def solution(rank, attend):
    a, b, c = [i for _, i in sorted([(r, i) for i, (r, att) in enumerate(zip(rank, attend)) if att])[:3]]
    return 10000*a + 100*b + c

# 다른 사람의 풀이1
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]

# 다른 사람의 풀이2_괜히 복잡하게 sorted(어쩌구) 하지 않는 코드
def solution(rank, attendance):
    selected = []
    for i, attend in enumerate(attendance):
        if attend:
            selected.append((rank[i], i))
    selected.sort()
    a, b, c = selected[:3]
    return 10000 * a[1] + 100 * b[1] + c[1]

# 다른 사람의풀이3
def solution(rank, attendance):
    lst = []
    for i in range(len(rank)):
        if attendance[i]:
            lst.append((rank[i],i))
    lst.sort()
    return 10000*lst[0][1]+100*lst[1][1]+lst[2][1]



