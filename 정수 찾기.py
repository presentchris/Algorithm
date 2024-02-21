#내 풀이1
def solution(num_list, n):
    for i in range(len(num_list)):
        if num_list[i]==n:
            return 1
    return 0

#내 풀이2
def solution(num_list, n):
    return int(n in num_list)

#내 풀이3
solution = lambda num_list, n : int(n in num_list)

#내 풀이4_리스트에 같은 요소가 두 개 있으면 틀린 풀이가 되기 때문에 일반화할 수는 없음
solution = lambda num_list, n : num_list.count(n)

#다른 사람의 풀이1_'n in num_list'의 결과가 True이면 [0, 1][1]이 되어 1이 반환
def solution(num_list, n):
    return [0,1][n in num_list]

