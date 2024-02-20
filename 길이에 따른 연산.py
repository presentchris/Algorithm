#내 풀이1
def solution(num_list):
    num = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in range(len(num_list)):
            num*=num_list[i]
        return num

#내 풀이2
def solution(num_list):
    num = 1
    for i in range(len(num_list)):
        num *= num_list[i]
    return sum(num_list) if len(num_list) >= 11 else num

#내 풀이3
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else eval("*".join(map(str, num_list)))

#내 풀이4
solution = lambda num_list : sum(num_list) if len(num_list) >= 11 else eval("*".join(map(str, num_list)))

#다른 사람의 풀이1_그냥 import를 하는게 아니라 'from math import prod'를 해야 함
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)

#다른 사람의 풀이2_마찬가지로 곱하는 함수를 쓰기 위해서 'from functools import reduce', 그리고 reduce 안에다가 list 변수를 넣는게 아니라 lambda와 같이 사용
from functools import reduce
def solution(l):
    return sum(l) if len(l)>=11 else reduce(lambda a,b: a*b, l)

#다른 사람의 풀이3_길어지긴 하지만 아예 곱셈 함수를 만들어서 사용하는 방식도 흥미로움
def mul(l):
    r = 1
    for i in l:
        r *= i
    return r
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else mul(num_list)