# 내 풀이1
def solution(n, control):
    answer=n
    for i in control:
        if i == "w":
            answer+=1
        elif i == "s":
            answer-=1
        elif i == "d":
            answer+=10
        elif i == "a":
            answer-=10        
    return answer

# 내 풀이2
def solution(n, control):
    for i in control:
        if i == "w":
            n+=1
        elif i == "s":
            n-=1
        elif i == "d":
            n+=10
        else:
            n-=10        
    return n

# 내 풀이3
def solution(n, control):
    return sum([n+1 if i == "w" else n-1 if i == "s" else n+10 if i == "d" else n-10 for i in control])

# 내 풀이4
def solution(n, control):
    return n+sum(1 if i == "w" else -1 if i == "s" else 10 if i == "d" else -10 for i in control)

# 다른 사람의 풀이1_dict와 zip을 이용하는 방법
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

# 다른 사람의 풀이2
ef solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

# 다른 사람의 풀이3
def solution(n, control):
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))

# 다른 사람의 풀이4
def solution(n, control):
    control_dict = {'w' : "1" , 's' : "-1", 'd' : "10", 'a' : "-10"}
    return eval("+".join(control_dict[letter] for letter in control)) + n

# 다른 사람의 풀이5
def solution(n, control):
    for c in control:
        if c=='w':n+=1
        elif c=='s':n-=1
        elif c=='d':n+=10
        else:n-=10
    return n

# GPT 코드_4번과 같이 문자열로 써서 join을 하지 않고, 정수형으로 나타내어 get메서드를 사용, control에 문자열이 없으면 0 반환
def solution(n, control):
    control_dict = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    result = 0
    for i in control:
        result += control_dict.get(i, 0)
    return result + n
