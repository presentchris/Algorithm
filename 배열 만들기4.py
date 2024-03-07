#내 풀이_틀린 풀이;[1]의 결과가 나옴
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk)==0 or stk[-1] < arr[i]:
            stk.append(arr[i])
        elif stk[-1] >= arr[i]:
            stk.remove(stk[-1])
    return stk

#내 풀이2_gpt풀이, 이해를 못하겠음, 일반화되지 않을 수 있는 풀이
def solution(arr):
    if not arr:  # 배열이 비어있으면 빈 배열 반환
        return []

    stk = [arr[0]]  # 첫 번째 요소로 시작
    for i in range(1, len(arr)):
        # 현재 요소가 stk의 마지막 요소보다 크면 추가
        if arr[i] > stk[-1]:
            stk.append(arr[i])
        # 현재 요소가 stk의 마지막 요소보다 작거나 같고, stk 길이가 1보다 크며, 
        # 현재 요소가 stk의 끝에서 두 번째 요소보다 크면 마지막 요소 교체
        elif len(stk) > 1 and arr[i] > stk[-2]:
            stk[-1] = arr[i]
    return stk

#내 풀이3_gpt도움으로 맞춘 풀이
def solution(arr):
    stk = []
    for i in arr:
        # 스택이 비어 있지 않고 스택의 마지막 요소가 현재 요소보다 크거나 같으면 제거
        while stk and stk[-1] >= i:
            stk.pop()
        # 현재 요소를 스택에 추가
        stk.append(i)
    return stk

#내 풀이4_내가 원래 구현하려고 했던 정답 풀이
def solution(arr):
    stk = []
    for i in arr:
        while len(stk)>0 and stk[-1] >= i:
            stk.remove(stk[-1])
        stk.append(i)
    return stk

#다른 사람의 풀이1_for를 사용하지 않고, while과 if조건문으로만 풀이
def solution(arr):
    stk = []
    i = 0

    arr_size = len(arr)

    while i < arr_size:
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()

    return stk

#다른 사람의 풀이2_for, while, 연달아 쓴 elif
def solution(arr):
    stk = []

    for i in range(len(arr)):
        while True:
            if len(stk) == 0:
                stk.append(arr[i])
                break
            elif stk[-1] < arr[i]:
                stk.append(arr[i])
                break
            elif stk[-1] >= arr[i]:
                stk.pop()

    return stk

#다른 사람의 풀이3_i 초기화 선언 후 while에서 i 사용, del은 변수나 리스트의 요소, 슬라이스 등을 삭제하는 데 사용, 인덱스나 슬라이스를 사용하여 리스트의 특정 요소나 범위를 삭제 
def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if stk==[]:
            stk.append(arr[i])
            i+=1
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        elif stk[-1]>=arr[i]:
            del stk[-1]

    return stk