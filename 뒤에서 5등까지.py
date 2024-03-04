#내 풀이1
solution = lambda num_list: sorted(num_list)[:5]

#내 풀이2_슬라이싱을 이용하지 않고 인덱스를 이용하여 5개까지만 추출하는 방법
def solution(num_list):
    answer=[]
    asc = sorted(num_list)
    for i in range(len(asc)):
        answer.append(asc[i]) if i<5 else None
    return answer

#내 풀이3_선택정렬
def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

def solution(num_list):
    selection_sort(num_list)
    answer = []
    for i in range(min(5, len(num_list))):
        answer.append(num_list[i])
    return answer

#내 풀이4_삽입정렬
def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        while j >= 0 and key < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key

def solution(num_list):
    insertion_sort(num_list)
    answer = []
    for i in range(min(5, len(num_list))):
        answer.append(num_list[i])
    return answer

#내 풀이5_퀵 정렬
def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    pivot = num_list[len(num_list) // 2]
    left = [x for x in num_list if x < pivot]
    middle = [x for x in num_list if x == pivot]
    right = [x for x in num_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def solution(num_list):
    sorted_list = quick_sort(num_list)
    return sorted_list[:5] if len(sorted_list) >= 5 else sorted_list

#내 풀이6_병합정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 리스트를 반으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 재귀적으로 각 부분 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 정렬된 두 부분을 병합
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # 왼쪽과 오른쪽 리스트를 비교하면서 작은 값을 결과에 추가
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # 남은 요소 추가
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

def solution(num_list):
    sorted_list = merge_sort(num_list)
    return sorted_list[:5] if len(sorted_list) >= 5 else sorted_list

#다른 사람의 풀이1
def solution(num_list):
    answer = []
    for i in range(5):
        answer.append(min(num_list))
        num_list.remove(min(num_list))
    return answer

#다른 사람의 풀이2
def solution(num_list):
    answer = []
    num_list.sort()
    for i in range(0, 5):
        answer.append(num_list[i])
    return answer

 #다른 사람의 풀이3
def solution(num_list):
    return [_ for k, _ in enumerate(list(sorted(num_list))) if k < 5]

#다른 사람의 풀이4
def solution(num_list):
    return [i for i, j in zip(sorted(num_list), range(len(num_list))) if j < 5]