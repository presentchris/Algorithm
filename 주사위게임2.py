#내 풀이1_정확하지 않은 풀이
def solution(a, b, c):
    if a!=b!=c:
        return a+b+c
    elif a==b==c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        return (a+b+c)*(a**2+b**2+c**2)

#내 풀이2_정확하지 않은 풀이
def solution(a, b, c):
    return a+b+c if a!=b!=c else((a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3) if a==b==c else (a+b+c)*(a**2+b**2+c**2))

#고친 풀이
def solution(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b != c or a != b == c or a == c != b:
        return (a + b + c) * (a**2 + b**2 + c**2)

#다른 사람의 풀이1
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)

#다른 사람의 풀이2
def solution(a, b, c):
    answer=a+b+c
    if a==b or b==c or a==c: answer*=a**2+b**2+c**2
    if a==b==c:answer*=a**3+b**3+c**3
    return answer

#다른 사람의 풀이3
solution = lambda a, b, c: a+b+c if a!=b and b!=c and c!=a else ((a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3) if a==b and b==c else (a+b+c)*(a**2+b**2+c**2))

#다른 사람의 풀이4
def solution(a, b, c):
    list = [a, b, c]
    answer = 1
    for i in range(4-len(set(list))):
        answer *= a**(i+1)+b**(i+1)+c**(i+1)
    return answer

