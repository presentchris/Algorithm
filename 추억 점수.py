# 내 풀이1_에러나는 코드, j는 문자열이기 때문에 name[j] 또는 photo[j]처 인덱스처럼 썼을 때 타입 에러가 남, 초기화한 score값의 위치(들여쓰기)와 answer.append(score)값의 위치가 잘못됨.
def solution(name, yearning, photo):
    answer = []
    score = 0
    d = dict(zip(name, yearning))
    for i in photo:
        for j in i:
            if name[j] in photo[j]:
                score += yearning[j]
            answer.append(score)
    return answer

# 내 풀이2_gpt 도움으로 수정한 코드
def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))  # 이름과 yearning 값을 매핑
    for i in photo:  # 각 사진 줄을 순회
        score = 0  # 각 사진 줄마다 점수를 계산하기 위해 여기서 초기화
        for j in i:  # 사진 줄의 각 이름을 순회
            if j in d:  # 만약 현재 이름이 d 딕셔너리의 키 중 하나라면
                score += d[j]  # 해당 이름에 대응하는 yearning 값을 점수에 더함
        answer.append(score)  # 각 사진 줄에 대한 최종 점수를 answer에 추가
    return answer

# 내 풀이3_sum()의 괄호가 for문과 if문을 어디까지 묶는지 살펴야 한다. d[j]는 단일 정수 값이기 때문에, sum 함수를 이 값에 적용할 수 없음. score를 초기화하고 +=를 어디서 하는지를 이해하면 됨. 그리고 그렇게 더한 것들을 요소로 나열하기 때문에 for i in photo 전까지 sum()을 적용한다.
def solution(name, yearning, photo):
    d = dict(zip(name, yearning))
    return [sum(d[j] for j in i if j in d) for i in photo]

# 다른 사람의 풀이1_딕셔너리가 아닌 index를 사용한 방식
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]

# 다른 사람의 풀이2_x==name이니까 score_dict[x]==해당 이름의 yearning이므로 map으로 해당하는 점수 계산하여 출력하고 sum으로 합산
def solution(name, yearning, photo):
    score_dict = dict(zip(name,yearning))
    return [sum(map(lambda x: score_dict[x] if x in score_dict else 0,p)) for p in photo]
