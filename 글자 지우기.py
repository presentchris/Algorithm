'''
사용 가능한 함수 및 로직
1. replace
2. re.sub
*strip, rstrip, lstrip 등은 해당하는 문자를 모두 지우기 때문에 이 경우에 사용할 수는 없을 것

# 예1
def solution(my_string, indices):    
    return my_string.replace(my_string[indices[0]], "")

# 예2
import re

def solution(my_string, indices):    
    return re.sub(my_string[indices[0]], "", my_string)
'''

# 내 풀이1
