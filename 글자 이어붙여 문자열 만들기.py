#1
def solution(my_string, index_list):
    answer = ''
    for i in index_list:  # index_list의 각 요소를 순회
        if 0 <= i < len(my_string):  # 유효한 인덱스인지 확인
            answer += my_string[index]  # 유효한 인덱스에 해당하는 문자를 answer에 추가
    return answer

#다른 사람의 풀이2
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

#다른 사람의 풀이3
def solution(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))

#다른 사람의 풀이4
def solution(my_string, index_list):
    res=''
    for i in index_list: res+=my_string[i]
    return res

#다른 사람의 풀이5
def solution(my_string, index_list):
    answer = ""
    for i in index_list:
        answer += my_string[i]
    return answer