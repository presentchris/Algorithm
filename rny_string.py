#내 풀이1
def solution(rn):
    return rn.replace("m","rn") if "m" in rn else rn

#내 풀이2
solution = lambda rn: rn.replace("m","rn") if "m" in rn else rn

#내 풀이3
solution = lambda rn: ''.join(i.replace("m","rn") if i=="m" else i for i in rn)

#내 풀이4
def solution(rn):
    k=''
    for i in rn:
        if i=='m':
            k+='rn'
        else:
            k+=i
    return k

#내 풀이5
solution = lambda rn: ''.join("rn" if i=="m" else i for i in rn)

#내 풀이6
solution = lambda rn: rn.replace("m", "rn") if rn.count("m")>=1 else rn

#다른 사람의 풀이1
def solution(rny_string):
    return rny_string.replace('m', 'rn')

#다른 사람의 풀이2
def solution(rny_string):
    answer = []
    for x in rny_string:
        if x=='m': answer.append('rn')
        else: answer.append(x)
    return ''.join(answer)

