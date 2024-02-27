#내 풀이1
def solution(num_list, n):
    return num_list[:n]

#내 풀이2
solution = lambda l,n: l[:n]

#다른 사람의 풀이1
def solution(num_list, n):
    return [v for i,v in enumerate(num_list) if i<n]

#다른 사람의 풀이2
def solution(num_list, n):
    answer = [ num_list[i] for i in range(n) ]
    return answer