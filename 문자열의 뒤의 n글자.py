#내 풀이1
def solution(my_string, n):
    return my_string[-n:]

#내 풀이2
solution = lambda my_string, n : my_string[-n:]

#다른 사람의 풀이1
solution = lambda my_string, n:my_string[len(my_string)-n:]

#다른 사람의 풀이2
def solution(my_string, n):
    answer = ''
    my_list = list()
    for i in my_string:
        my_list.append(i)


    for j in range(len(my_string)-n, len(my_string)):
        answer += my_list[j]


    return answer