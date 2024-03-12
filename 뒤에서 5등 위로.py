# 내 풀이
def solution(num_list):
    small = sorted(num_list)[:5]
    for i in small:
        num_list.remove(i)
    return sorted(num_list)

# gpt의 복잡한 풀이_간결하게 해달랬는데 더 길어짐
from collections import Counter

def solution(num_list):
    # 각 요소별 등장 횟수 계산
    count = Counter(num_list)
    # 가장 작은 5개의 요소 찾기
    smallest = sorted(count.keys())[:5]

    # 가장 작은 5개의 요소를 제외한 나머지 요소만 포함하는 리스트 생성
    new_list = [x for x in num_list if x not in smallest or count[x] > 0 and count.update({x: count[x]-1})]

    return sorted(new_list)

# gpt의 다른 풀이_heapq.nsmallest와 if else 형식이 아닌 if와 or를 가지고 새로운 로직을 구현한 것이 신기함
import heapq

def solution(num_list):
    # 가장 작은 5개의 요소를 찾음
    small = heapq.nsmallest(5, num_list)
    # 가장 작은 5개의 요소를 제외한 나머지 요소만 포함하는 새 리스트 생성
    remain = [x for x in num_list if x not in small or small.remove(x)]
    
    return sorted(remain)

# 다른 사람의 풀이1_remove하지 않고 슬라이싱을 반대로 [5:] 처럼 이용해도 되는데 왜 더 복잡하게 풀었는지 스스로가 이해 안 감
def solution(num_list):
    return sorted(num_list)[5:]

# 다른 사람의 풀이2
def solution(num_list):
    answer = []
    a=min(num_list)
    num_list.remove(a)
    b=min(num_list)
    num_list.remove(b)
    c=min(num_list)
    num_list.remove(c)
    d=min(num_list)
    num_list.remove(d)
    e=min(num_list)
    num_list.remove(e)
    return sorted(num_list)

# 다른 사람의 풀이3_sorted와 반복문, pop을 이용한 풀이
def solution(num_list):
    answer = []
    a=sorted(num_list)
    for i in range(5):
        a.pop(0)
    return a
