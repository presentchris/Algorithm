# 내 풀이1_이번에도 return 위치 신경쓰기, 차근 차근 테스트해보며 내 힘으로 풀 수 있다
def solution(my_strings, parts):
    answer = ''
    for i, (s, e) in zip(my_strings, parts):
        answer += i[s:e+1]
    return answer

# 내 풀이2_코드 간략
solution = lambda my_string, part: ''.join(i[s:e+1] for i, (s, e) in zip(my_string, part))

# 내 풀이3_parts 부분을 part라는 임의 변수로 반복문 안에 지정해서 part[0]과 part[1]과 같이 나타내는 방법
solution = lambda my_string, parts: ''.join(i[part[0]:part[1]+1] for i, part in zip(my_string, parts))

# 다른 사람의 풀이1_'my_strings[i][s:e+1]'를 사용한 방법
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer

# 다른 사람의 풀이2_'my_strings[i][parts[i][0]:parts[i][1]+1]'처럼 변수를 선언하지 않고 parts의 리스트 길이= 요소 길이에 따라 변수를 i로 두고 i 하나만을 이용하여 슬라이싱한 방법
def solution(my_strings, parts):
    answer = ""
    for i in range(len(parts)):
        answer += (my_strings[i][parts[i][0]:parts[i][1] + 1])
    return answer
