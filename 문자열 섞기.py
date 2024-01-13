# 내 풀이_틀린 코드
# def solution(str1, str2):
#     for i in str1:
#         for k in str2:
#             answer = (i + k) * len(str1)
#     return answer

# 다른 사람의 풀이1
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer

# 다른 사람의 풀이2
def solution(str1, str2):
    res=''
    for s1,s2 in zip(str1,str2):
        res+=s1+s2
    return res

# 다른 사람의 풀이3
def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer

# 다른 사람의 풀이4
def solution(str1, str2):
    return ''.join(i+j for i,j in zip(str1,str2))

# 다른 사람의 풀이5
def solution(str1, str2):
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return ''.join(answer)

# 다른 사람의 풀이6
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer+=str1[i]+str2[i]
    return answer


