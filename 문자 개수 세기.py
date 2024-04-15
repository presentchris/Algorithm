# 내 풀이1
def solution(my_string):
    ans = [0] * 52
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    whole = upper + [char.lower() for char in upper]
    ref = {i: idx for idx, i in enumerate(whole)}
    for i in my_string:
        if i in ref:
            ans[ref[i]] += 1
    return ans

# 내 풀이2
from collections import Counter
def solution(my_string):
    counts = Counter(my_string)    
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return [counts[char] for char in alphabet]

# 다른 사람의 풀이1
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer

# 다른 사람의 풀이2
def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']

# 다른 사람의 풀이3
def solution(my_string):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        answer.append(len(my_string.split(i))-1)
    return answer

# 다른 사람의 풀이4
import string
def solution(my_string):
    count = dict.fromkeys(string.ascii_uppercase + string.ascii_lowercase, 0)
    for s in my_string:
        count[s] += 1
    return list(count.values())
