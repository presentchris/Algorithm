# 첫 번째 코드
def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(s, len(my_string)+1):
        answer = my_string[:s] + overwrite_string + my_string[len(overwrite_string)+s:] 
    return answer


# 두 번째 코드
# def solution(my_string, overwrite_string, s):
#     answer = ''
#     for i in range(s, len(my_string)+1):
#         answer = my_string.replace(f"{my_string[s:]}",f"{overwrite_string}") + my_string[s+len(overwrite_string):]
#     return answer

# 다른 사람의 풀이1
# def solution(my_string, overwrite_string, s):
#     answer = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
#     return answer

# 다른 사람의 풀이2
# def solution(my_string, overwrite_string, s):
#     return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

# 다른 사람의 풀이3
# def solution(my_string, over, s):
#     a=list(my_string)
#     b=list(over)
#     a[s:s+len(b)]=b
#     return ''.join(a)
