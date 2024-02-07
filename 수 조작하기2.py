#내 풀이1
def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i]==numLog[i+1]-1: answer+='w'
        elif numLog[i]==numLog[i+1]+1: answer+='s'
        elif numLog[i]==numLog[i+1]-10: answer+='d'
        else: answer+='a'
    return answer

#내 풀이2
def solution(numLog):
    answer = []
    for i in range(len(numLog)-1):
        if numLog[i]==numLog[i+1]-1:
            answer.append('w')
        elif numLog[i]==numLog[i+1]+1:
            answer.append('s')
        elif numLog[i]==numLog[i+1]-10:
            answer.append('d')
        elif numLog[i]==numLog[i+1]+10:
            answer.append('a')
    return ''.join(answer)

#내 풀이3_문자열에서는 sum이 아니라  join을 쓸 수 있음
def solution(numLog):
    return ''.join(['w' if numLog[i]==numLog[i+1]-1 else 's' if numLog[i]==numLog[i+1]+1 else 'd' if numLog[i]==numLog[i+1]-10 else 'a' for i in range(len(numLog)-1)])

#다른 사람의 풀이1
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

#다른 사람의 풀이2
def solution(numLog):
    return "".join(["w" if numLog[i] - numLog[i - 1] == 1 else "s" if numLog[i] - numLog[i - 1] == -1 else "d" if numLog[i] - numLog[i - 1] == 10 else "a" for i in range(1, len(numLog))])