# 내 풀이1_s+1을 했는데 슬라이싱 안에서 처음이든 마지막이든 인덱스를 따르기 때문에 s를 해야 함. 그리고 k와 비교할 때 int처리를 안해서 str과 int를 비교할 수 없기 때문에 에러가 났음. 타입도 주의해야 함.
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer

# 내 풀이2_코드 간략화
solution = lambda intStrs, k, s, l: [int(i[s:s+l]) for i in intStrs if int(i[s:s+l]) > k]

# 다른 사람의 풀이1
def solution(intStrs, k, s, l):
    answer = []
    temp=''
    for i in range(len(intStrs)):
        temp=intStrs[i][s:][:l]
        if int(temp)>k:
            answer.append(int(temp))
    return answer

'''다른 사람의 풀이2_"map(lambda x: x * 2, [1, 2, 3])"은 [1, 2, 3] 각 요소에 lambda x: x * 2 함수를 적용하여 [2, 4, 6]을 생성하고, 
"filter(lambda x: x > 2, [1, 2, 3, 4])"은 [1, 2, 3, 4] 각 요소 중 lambda x: x > 2 조건을 만족하는 [3, 4]만을 선택.
map은 모든 요소에 함수를 적용한 결과를 반환하는 반면, filter는 조건을 만족하는 요소만을 선택.
map은 데이터에 변환을 적용할 때 사용되며, filter는 데이터를 필터링할 때 사용됨.
map은 함수의 적용 결과에 대한 새로운 시퀀스를 생성하며, filter는 기존 시퀀스에서 조건을 만족하는 요소만을 포함하는 새로운 시퀀스를 생성.
sorted(), min(), max() 등에서 쓰이는 key=lambda 와 구별하기. 이외에도 key=lambda를 사용하는 함수로는 heapq.nlargest()와 heapq.nsmallest(), itertools.groupby()가 있음.'''
def solution(intStrs, k, s, l):
    return list(filter(lambda x: x > k, map(lambda x: int(x[s:s + l]), intStrs)))
