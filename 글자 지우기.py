'''
글자를 지울 때 사용 가능한 함수 및 로직
1. replace
2. re.sub
3. strip(양끝단 / 위치에 따라 rstrip, lstrip)
*strip, rstrip, lstrip 등과 위 함수들은 해당하는 문자를 모두 지우기 때문에 이 경우에 사용할 수는 없을 것

# 예1
def solution(my_string, indices):    
    return my_string.replace(my_string[indices[0]], "")

# 예2
import re

def solution(my_string, indices):    
    return re.sub(my_string[indices[0]], "", my_string)
'''

# 내 풀이1
def solution(my_string, indices):
    ans = ''
    for i in range(len(my_string)):
        if i not in indices:
            ans += my_string[i]
    return ans

# 다른 사람의 풀이1
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)


# 다른 사람의 풀이2
def solution(my_string, indices):
    return "".join([v for i,v in enumerate(my_string) if i not in indices])


# 다른 사람의 풀이3_replace 안 쓰고 X를 ''로 바로 바꿀 수 있음
def solution(my_string, indices):
    for idx in indices:
        my_string = my_string[:idx] + 'X' + my_string[idx+1:]
    return my_string.replace('X', '')
