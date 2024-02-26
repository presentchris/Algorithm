#내 풀이1
def solution(num_list, n):
    return num_list[n-1:]

#내 풀이2
solution = lambda num_list,n: num_list[n-1:]

#다른 사람의 풀이1
def solution(num_list, n):
    answer = []
    for i in range(n-1,len(num_list)):
        answer.append(num_list[i])
    return answer

#다른 사람의 풀이2
def solution(num_list, n):
    return [num_list[i] for i in range(n - 1, len(num_list))]