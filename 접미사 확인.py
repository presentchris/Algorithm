# 내 풀이1_모든 예시에 정답을 도출할 수는 없을 것 같다
def solution(my_string, is_suffix):
    return int(my_string[0] not in is_suffix and my_string[-1] == is_suffix[-1])

# 내 풀이2_return 0 위치 때문에 계속 오류남. 들여쓰기 주의. my_string[0] not in is_suffix 조건은 접미사를 검사하는 데 필요하지 않다고 함.
def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if is_suffix==my_string[i:] and my_string[0] not in is_suffix:
            return 1
    return 0

# 내 풀이3_gpt 도움_처음엔 이 함수를 잘 몰라 is_suffix.endswith(my_string)으로 구현하거나 startswith까지 대동하기도 했다
solution = lambda my_string, is_suffix: int(my_string.endswith(is_suffix))

# gpt 풀이
def solution(my_string, is_suffix):
    # my_string의 마지막 len(is_suffix) 문자가 is_suffix와 일치하는지 확인
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else:
        return 0

# gpt 풀이 간략
def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)

# 다른 사람의 풀이1_[::-1]는 역순으로 뒤집는 것을 뜻함. 효율적인 풀이가 될 수 있음
def solution(my_string, is_suffix):
    return 1 if my_string[::-1][:len(is_suffix)]==is_suffix[::-1] else 0

# 다른 사람의 풀이2
def solution(my_string, is_suffix):
    answer = 0
    if my_string[len(my_string)-len(is_suffix):len(my_string)]==is_suffix:
        answer=1
    else:
        answer=0
    return answer

# 다른 사람의 풀이3_-1을 is_suffix의 길이에 곱해서 my_string에서 뒤에서부터 몇 번째 문자부터 시작할지를 결정하는 음수 인덱스를 생성
def solution(my_string, is_suffix):
    if my_string[-1*(len(is_suffix)):] == is_suffix:
        return 1
    return 0



